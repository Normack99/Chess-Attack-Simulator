from chess_pieces import Piece, COL_VALS

# Models a chess board
class ChessBoard:

    # Constructor to the ChessBoard class
    # Creates a table containing an 8 x 8 grid of dots "."
    def __init__(self):
        self.board = []
        for _ in range(8):
            self.board.append(["."] * 8)

    # Adds an object of type piece to the board at its given position
    # @param piece: any type of previously defined chess Piece
    def add(self, piece: Piece):
        self.board[8 - piece.row][piece.col_val] = piece
    
    # Displays the given chess board in its current state
    def display(self):
        for row in self.board:
            for col in row:
                print(col, end = "")
            print()

    # Gets the item at the specified board position
    # @param the row number of the specified position
    # @param the column letter of the specified position
    # @return the item on the board at the given row and column position
    def get_item(self, row: int, col: str):
        return self.board[8 - row][COL_VALS[col]]

    # Provides python built in functionality for determining the length of an object of type ChessBoard
    # @return the length of the given board's board list variable
    def __len__(self):
        return len(self.board)