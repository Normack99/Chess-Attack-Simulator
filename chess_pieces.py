COL_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]
PIECE_TYPES = ["K", "N", "Q", "B", "R", "P", "X"]

# Converts letter column values to integer numbers that can be compared
COL_VALS = { "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
}

# Models a chess piece
class Piece:

    # Constructor to the piece class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        self.row = row # adjusted to make sense with board indexes
        self.col = col
        self.col_val = COL_VALS[col] # col adjusted to an integer to compare board indexes
        self.type = ""

    # Returns the type of the given piece
    # @return the type of the piece
    def get_type(self) -> str:
        return self.type

    # Returns the row value of a given piece
    # @return the row of the piece
    def get_row(self) -> int:
        return self.row

    # Returns the column letter of a given piece
    # @return the column of the piece
    def get_col(self) -> str:
        return self.col
    
    # Returns the "identifier" of the given piece, represented by a string containing its type, column letter, and row number
    # @return a string containing the piece's type, column value, and row value. Ex: "Qb2"
    def get_identifier(self) -> str:
        return self.type + self.col + str(self.row)

    # Provides python built in functionality for converting the piece object to a type string (used when printing an object of type Piece)
    # @return a string containing the type of the given piece
    def __str__(self) -> str:
        return self.type
    
# Models a King piece. Inherits from Piece
class King(Piece):

    # Constructor to the King class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "K"

    # Given a VALID target row and column, determines whether the given king can attack that space
    # @param tr: the target row
    # @param tc: the target column
    # @return a bool value that determines whether the given king can attack the input space
    def can_attack(self, tr: int, tc: int) -> bool:
        tc_val = COL_VALS[tc]

        # A king can move one space in any direction (vertically)
        if tr == self.row + 1 and tc_val == self.col_val: return True
        elif tr == self.row - 1 and tc_val == self.col_val: return True

        # A king can move one space in any direction (horizontally)
        elif tc_val == self.col_val + 1 and tr == self.row: return True
        elif tc_val == self.col_val - 1 and tr == self.row: return True

        return False

# Models a Rook piece. Inherits from Piece  
class Rook(Piece):

    # Constructor to the Rook class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "R"

    # Given a VALID target row and column, determines whether the given rook can attack that space
    # @param tr: the target row number
    # @param tc: the target column letter
    # @return a bool value that determines whether the given rook can attack the input space
    def can_attack(self, tr: int, tc: str) -> bool:

        # A rook can move any number of spaces either 
        if tr == self.row: return True # vertically
        elif tc == self.col: return True # or horizontally
        return False
    
# Models a Bishop piece. Inherits from Piece  
class Bishop(Piece):

    # Constructor to the Bishop class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "B"

    # Given a VALID target row and column, determines whether the given bishop can attack that space
    # @param tr: the target row number
    # @param tc: the target column letter
    # @return a bool value that determines whether the given bishop can attack the input space
    def can_attack(self, tr: int, tc: str) -> bool:
        tc_val = COL_VALS[tc]

        # A bishop can move any number of spaces diagonally
        for factor in range(-7, 8): # loop from -7 to 7 (the maximum amount of valid diagonal spaces) and update both row and column values by the same factor
            if tr == self.row + factor and tc_val == self.col_val + factor: return True # Diagonally right up and left down (add/subtract the same factor from both the row and col value)
            elif tr == self.row - factor and tc_val == self.col_val + factor: return True # Diagonally left up and right down (add/subtract the opposite sign but same magnitude factor from both the row and col value)

        return False
    
# Models a Queen piece. Inherits from Piece 
class Queen(Piece):

    # Constructor to the Queen class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "Q"

    # Given a VALID target row and column, determines whether the given queen can attack that space
    # @param tr: the target row number
    # @param tc: the target column letter
    # @return a bool value that determines whether the given queen can attack the input space
    def can_attack(self, tr: int, tc: str) -> bool:

        # Can move any number of spaces in any direction. The queen is a combination of both the rook and bishop
        if Bishop.can_attack(self, tr, tc) == True or Rook.can_attack(self, tr, tc) == True: return True

# Models a Knight piece. Inherits from Piece 
class Knight(Piece):
    
    # Constructor to the Knight class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "N"

    # Given a VALID target row and column, determines whether the given knight can attack that space
    # @param tr: the target row number
    # @param tc: the target column letter
    # @return a bool value that determines whether the given knight can attack the input space
    def can_attack(self, tr: int, tc: str) -> bool:
        tc_val = COL_VALS[tc]

        # Can move two spaces vertically (upwards) followed by one space horizontally (left or right)
        if tr == self.row + 2 and tc_val == self.col_val + 1: return True
        elif tr == self.row + 2 and tc_val == self.col_val - 1: return True

        # Can move two spaces vertically (downwards) followed by one space horizontally (left or right)
        elif tr == self.row - 2 and tc_val == self.col_val + 1: return True
        elif tr == self.row - 2 and tc_val == self.col_val - 1: return True

        # Can move two spaces horizontally (up or down) followed by one space vertically (up)
        elif tr == self.row + 1 and tc_val == self.col_val + 2: return True
        elif tr == self.row + 1 and tc_val == self.col_val - 2: return True

        # Can move two spaces horizontally (up or down) followed by one space vertically (down)
        elif tr == self.row - 1 and tc_val == self.col_val + 2: return True
        elif tr == self.row - 1 and tc_val == self.col_val - 2: return True

        return False
    
# Models a Pawn type of chess piece. Inherits from Piece 
class Pawn(Piece):

    # Constructor to the Pawn class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "P"

    # Given a VALID target row and column, determines whether the given pawn can attack that space
    # Does not include en-passent rulings
    # @param tr: the target row number
    # @param tc: the target column letter
    # @return a bool value that determines whether the given pawn can attack the input space
    def can_attack(self, tr: int, tc: str) -> bool:
        tc_val = COL_VALS[tc]

        # Can only attack a square which is one space forwards and one space either to the left or right
        if tc_val == self.col_val + 1 and tr == self.row + 1: return True
        elif tc_val == self.col_val - 1 and tr == self.row - 1: return True

        return False

# Models a Marker to place on a chess board. Inherits from Piece 
class Marker(Piece):
    
    # Constructor to the Marker class
    # @param row: the row number of the piece
    # @param col: the column letter of the piece 
    def __init__(self, row: int, col: str):
        super().__init__(row, col)
        self.type = "X"