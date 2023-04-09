import customtkinter as ctk


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Tic-Tac-Toe')
        self.appearance = ctk.set_appearance_mode('dark')
        self.padx = 5
        self.pady = 5
        self.buttons = [[], [], []]
        self.buttons_text = []
        self.create_button_texts()
        self.create_buttons()

        # Configure rows and columns for a 3x3 grid
        self.grid_rowconfigure('all', weight=0)
        self.grid_columnconfigure('all', weight=0)

        # Button for clearing the board and starting a new game
        self.new_game_button = ctk.CTkButton(self, text='New Game', height=50, font=(None, 20))
        self.new_game_button.grid(row=3, column=0, columnspan=3, padx=self.padx, pady=self.pady, sticky='nsew')

    # Creating the buttons for the board
    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = ctk.CTkButton(self, textvariable=self.buttons_text[row][col],
                                       font=(None, 50), height=100, width=100)
                button.grid(row=row, column=col, padx=self.padx, pady=self.pady, sticky='nsew')
                self.buttons[row].append(button)

    def create_button_texts(self):
        for i in range(3):
            self.buttons_text.append([ctk.StringVar(value='') for x in range(3)])
