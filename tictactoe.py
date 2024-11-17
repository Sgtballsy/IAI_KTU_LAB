import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def is_empty(self, pos):
        return self.board[pos] == ' '

    def make_move(self, pos):
        self.board[pos] = self.current_player

    def is_winner(self, player):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                                [0, 4, 8], [2, 4, 6]]              # Diagonals
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def evaluate(self):
        if self.is_winner('X'):
            return 10
        elif self.is_winner('O'):
            return -10
        else:
            return 0

    def minimax(self, depth, is_maximizing):
        score = self.evaluate()

        if score == 10 or score == -10 or self.is_full():
            return score

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.is_empty(i):
                    self.make_move(i)
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score

        else:
            best_score = math.inf
            for i in range(9):
                if self.is_empty(i):
                    self.make_move(i)
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_val = -math.inf
        best_move = -1

        for i in range(9):
            if self.is_empty(i):
                self.make_move(i)
                move_val = self.minimax(0, False)
                self.board[i] = ' '

                if move_val > best_val:
                    best_move = i
                    best_val = move_val

        return best_move

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], "|", self.board[i+1], "|", self.board[i+2])
            if i != 6:
                print("---------")

    def play_game(self):
        while True:
            self.print_board()

            if self.is_winner('X'):
                print("X wins!")
                break
            elif self.is_winner('O'):
                print("O wins!")
                break
            elif self.is_full():
                print("Draw!")
                break

            if self.current_player == 'X':
                pos = int(input("Enter your move (0-8): "))
                while not self.is_empty(pos):
                    pos = int(input("Invalid move. Enter again: "))
                self.make_move(pos)
            else:
                best_move = self.find_best_move()
                self.make_move(best_move)
            self.current_player = 'O' if self.current_player == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()