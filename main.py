from gui import Gui
import game


class App:
    def __init__(self):
        self.game = game.Game()
        self.board = self.game.create_board()
        self.gui = Gui()
        self.configure_buttons()
        self.gui.mainloop()

    def button_press(self, row, col):
        player = self.game.turn()
        # Adding the position to the board if the position is available
        if self.board[row][col] == '':
            self.game.add_to_board(self.board, player, row, col)
            self.update_button()
            if self.game.check_for_win(self.board, player):
                self.win()
            if self.game.check_if_full(self.board):
                self.draw()

    def update_button(self):
        for row in range(3):
            for col in range(3):
                self.gui.buttons_text[row][col].set(self.board[row][col])

    def win(self):
        combo = self.game.winning_combo()
        r1, c1, r2, c2, r3, c3 = combo
        rows = [r1, r2, r3]
        cols = [c1, c2, c3]
        for row in range(3):
            for col in range(3):
                self.gui.buttons[row][col].configure(fg_color=('#13293e', '#13293e'), state='disabled')
        for i in range(3):
            self.gui.buttons[rows[i]][cols[i]].configure(fg_color=('#3a7ebf', '#1f538d'))

    def draw(self):
        for row in range(3):
            for col in range(3):
                self.gui.buttons[row][col].configure(state='disabled')

    def new_game(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ''
        self.configure_buttons()
        self.update_button()
        self.game.player_one_turn = True
        self.game.winning_combination = None

    def configure_buttons(self):
        for row in range(3):
            for col in range(3):
                self.gui.buttons[row][col].configure(fg_color=('#3a7ebf', '#1f538d'),
                                                     state='normal',
                                                     command=lambda i=row, x=col: self.button_press(i, x))
        self.gui.new_game_button.configure(command=lambda: self.new_game())


if __name__ == '__main__':
    app = App()
