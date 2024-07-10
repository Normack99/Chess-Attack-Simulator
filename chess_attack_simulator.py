from chess_pieces import *
from chess_board import *

# Adds valid input pieces to the board until a marker is established 
# @param the board to add inputs to. Type: ChessBoard
# @return a tuple containing the target's row and column value
def add_inputs(board: ChessBoard) -> tuple:
    inpt_type = ""
    counts = {"K": 0,
        "N": 0,
        "Q": 0,
        "B": 0,
        "R": 0,
        "P": 0,
    }

    while inpt_type != "X": # Keep adding pieces until a target piece is added

        valid = True # For every loop, update valid back to true, until it is later determined to be false if the input is invalid

        try:
            
            inpt = input("Input a type of piece, column letter, and row number. (Ex. Qb2). Input a target (type X) to end the input stage: ")

            inpt_type = inpt[0].capitalize()# Capitalize the input piece, since the piece type strings in the program are all capitals
            inpt_col = inpt[1].lower() # Lower the input column, since the columns in this program are all lowercase
            inpt_row = int(inpt[2]) # Convert the input row to an integer

            print()


            if inpt_type in PIECE_TYPES and inpt_col in COL_LETTERS and inpt_row > 0 and inpt_row < 9 and board.get_item(inpt_row, inpt_col) == ".": # Check whether the input piece is valid

                if inpt_type in ["K", "Q"] and counts[inpt_type] >= 1: # Check whether the amount of kings/queens is valid
                    print("You have reached the maximum limit. There can only be 1 king or queen on the board at any given time\n")
                    continue
                elif inpt_type in ["B", "R", "N"] and counts[inpt_type] >= 2: # Check whether the amount of bishops, rooks, and knights is valid
                    print("You have reached the maximum limit. There can only be 2 bishops, rooks, or knights on the board at any given time\n")
                    continue
                elif inpt_type == "P" and counts[inpt_type] >= 8: # Check whether the amount of pawns is valid
                    print("You have reached the maximum limit. There can only be 8 pawns on the board at any given time\n")
                    continue

                match inpt_type:  # For every possible valid type of piece, add it to the board, passing in the input row and column values

                    case "K":
                        board.add(King(inpt_row, inpt_col))
                    case "N":
                        board.add(Knight(inpt_row, inpt_col))
                    case "Q":
                        board.add(Queen(inpt_row, inpt_col))
                    case "B":
                        board.add(Bishop(inpt_row, inpt_col))
                    case "R":
                        board.add(Rook(inpt_row, inpt_col))
                    case "P":
                        board.add(Pawn(inpt_row, inpt_col))
                    case "X":                                    # If a target is added, stop the loop and return its row and column values
                        board.add(Marker(inpt_row, inpt_col))
                        return (inpt_row, inpt_col)
                    
                counts[inpt_type] += 1 # Add 1 to the count of the given piece type

            else: # If the input is invalid, valid is false
                valid = False
    
        except: # If the input produces an error, it is invalid and valid is false
            valid = False

        if valid == False:
            print("Please enter a valid piece type, column letter, and row number. It must be in a position where there are no other pieces.\n")

# Calls all other functions and controls program flow
def main():

    print("This program will model a filled in chess board, with input pieces and an input target.\nIf the input pieces can attack the target, they are listed after the board is displayed (disregarding other pieces that may be in the way)\n")
    
    b = ChessBoard() # Create an object b of type ChessBoard

    target_row, target_col = add_inputs(b) # Add any number of pieces to the board, stopping when the target is established. Returns the target row and column values

    b.display() # Display the board
    print()
    print("The following pieces can attack the target position:")

    for row in range(1, 9): # Loop through every row from 1 to 8 
        for col in COL_LETTERS:     # Loop through each column in order (from left to right)
            item = b.get_item(row, col) # Get the item at the specified board position

            if type(item) != str and type(item) != Marker:  # If the item is not a piece and is a ".", an error will occur. This statement will catch the error 
                if item.can_attack(target_row, target_col): 
                    print(item.get_identifier())

if __name__ == "__main__":
    main() 