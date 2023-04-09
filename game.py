

class Game:
    def __init__(self):
        self.player_one = 'X'
        self.player_two = 'O'
        self.player_one_turn = True
        self.winning_combination = None

    def create_board(self):
        board = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]
        return board

    # Adds the player to the board at the row and column of the button the player chooses
    def add_to_board(self, board, player, row, column):
        board[row][column] = player

    # Checks the board for all the combinations the player could win with
    def check_for_win(self, board, player):
        # Checks rows for three across
        for row in range(len(board)):
            if board[row].count(player) == 3:
                self.winning_combination = (row, 0, row, 1, row, 2)
                return True
        # Checks through columns for three down
        for i in range(0, len(board)):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                self.winning_combination = (0, i, 1, i, 2, i)
                return True
        # checks for cross pattern from top left to bottom right
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            self.winning_combination = (0, 0, 1, 1, 2, 2)
            return True
        # checks for cross pattern from top right to bottom left
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            self.winning_combination = (0, 2, 1, 1, 2, 0)
            return True

    # checks to see if the board is full
    def check_if_full(self, board):
        for i in board:
            if '' in i:
                return False
        return True

    def turn(self):
        if self.player_one_turn:
            self.player_one_turn = False
            return self.player_one

        self.player_one_turn = True
        return self.player_two

    def winning_combo(self):
        return self.winning_combination

