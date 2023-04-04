from gui import Gui
import gui
import customtkinter as ctk
import game


class App:
    def __init__(self):
        self.game = game.Game()
        self.board = self.game.create_board()
        self.gui = Gui()
        self.gui.mainloop()
        print('hello')

    def button_press(self, row, col):
        player = self.game.turn()
        # Adding the position to the board if the position is available
        if self.board[row][col] == '':
            self.game.add_to_board(self.board, player, row, col)
            print(self.board)
            self.update_button()
            if self.game.check_for_win(self.board, player):
                self.win(player)
            if self.game.check_if_full(self.board):
                self.draw()

    def update_button(self):
        for i in range(0, len(self.board)):
            for x in range(0, len(self.board[i])):
                self.gui.buttons_text[i][x].set(self.board[i][x])

    def win(self, player):
        pass

    def draw(self):
        pass




if __name__ == '__main__':
    app = App()