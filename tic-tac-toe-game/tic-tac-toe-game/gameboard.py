class GameBoard:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        if self.board[row][col] == '':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self, player):
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True

        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        if all([self.board[i][i] == player for i in range(3)]):
            return True

        if all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True