from gui import Gui


class Game:
    def __init__(self):
        self.player_one = 'X'
        self.player_two = 'O'
        self.player_one_turn = True

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
        for row in board:
            if row.count(player) == 3:
                return True

        # Checks through columns for three down
        for i in range(0, len(board)):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return True

        # checks for cross pattern from top left to bottom right
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True

        # checks for cross pattern from top right to bottom left
        return board[0][2] == player and board[1][1] == player and board[2][0] == player

    # checks to see if the board is full
    def check_if_full(self, board):
        for i in board:
            if '' in i:
                return True
        return False

    def turn(self):
        if self.player_one_turn:
            self.player_one_turn = False
            return self.player_one

        self.player_one_turn = True
        return self.player_two
