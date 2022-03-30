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


class Game:
    def __init__(self):
        self.board = Board()
        self.points = [0, 0]
        self.turn = "x"
    def gameloop(self):
        while True:
            while True:
                self.play(self.turn)
                if self.board.check_winner():
                    if self.board.check_winner() == "x":
                        self.points[0] += 1
                        print("Player 1 won!")
                    if self.board.check_winner() == "O":
                        self.points[1] += 1
                        print("Player 2 won!")
                    break
            answer = input("Do you want to keep playing? (y/n)")
            if answer == 'n':
                break
    def play(self):
        self.board.print_board()
        coordinates = input("Please enter the two coordinates where you want to play, seperated by a comma (e.g. \"0,0\") and then press enter: ").split(",")
       self.board.move(self.turn, coordinates[0], coordinates[1])
       self.turn = "O" if self.turn == "x" else "x"
