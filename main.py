class Board:
    def __init__(self, board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]):
        self.__board = board 
    def print_board(self):
        for row in self.__board:
            print (*row, sep = " ")
    def get_board(self):
        return self.__board.copy()
    def move(self, player = "x", row=0, col=0):
        self.__board[row][col] = player
    def winner(self):
        for row in range(3):
            if self.check_row(row) and self.check_row(row) != " ":
                return self.check_row(row)
        for col in range(3):
            if self.check_col(col) and self.check_col(col) != " ":
                return self.check_col(col)
        for diagonal in ["+", "-"]:
            if self.check_diag(diagonal) and self.check_diag(diagonal) != " ":
                return self.check_diag(diagonal)
        return self.check_full()
    def reset(self):
        this.__board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    def check_row(self, row):
        piece = self.__board[row][0]
        for el in self.__board[row]:
            if el != piece:
                return False
        return piece

    def check_col(self, col):
        piece = self.__board[0][col]
        for i in range(3):
            if self.__board[i][col] != piece:
                return False
        return piece
    def check_diag(self, diag):
        if diag == "+":
            if self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
                return self.__board[0][0]
            return False

        if diag == "-":
            if self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
                return self.__board[0][0]
            return False
    def check_full(self):
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == " ":
                    return False
        return True


board = Board()
board.print_board()
board.move()
board.move("O", 1, 1)
board.print_board()
