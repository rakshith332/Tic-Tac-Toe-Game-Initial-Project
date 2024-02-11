class TicTacToe:
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.current_player = 'X'
        self.game_over = False

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))

    def check_winner(self, player):
        # Conditional Statements
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Slicing
        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def make_move(self, row, col):
        # Conditional Statements
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    # Recursion Function
    def play_game(self):
        while not self.game_over:
            self.display_board()

            # Get the player's move
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if not self.make_move(row, col):
                print("Invalid move")
                continue

            # Map Filter Reduce
            if self.check_winner(self.current_player):
                self.display_board()
                print(self.current_player + " wins!")
                self.game_over = True
            else:
                if all('-' not in row for row in self.board):
                    self.display_board()
                    print("Tie game!")
                    self.game_over = True
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
#main 
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()


