import customtkinter as ctk


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = 'Tic-Tac-Toe'
        self.appearance = ctk.set_appearance_mode('dark')
        self.padx = 15
        self.pady = 15
        self.buttons = []
        self.buttons_text = []
        self.create_button_texts()
        self.create_buttons()
        self.set_button_texts()

        # Configure rows and columns for a 3x3 grid
        self.grid_rowconfigure('all', weight=0)
        self.grid_columnconfigure('all', weight=0)

        # Creating the buttons for the board
    def create_buttons(self):
        for i in range(0, 3):
            self.buttons.append([ctk.CTkButton(self, text=self.buttons_text[i][x]).grid(
                                                                                        row=i,
                                                                                        column=x,
                                                                                        padx=self.padx,
                                                                                        pady=self.pady,
                                                                                        sticky='nsew'
                                                                                        ) for x in range(0, 3)])

    def create_button_texts(self):
        for i in range(0, 3):
            self.buttons_text.append([ctk.StringVar() for x in range(0, 3)])

    def set_button_texts(self):
        for i in range(0, 3):
            for x in range(0, 3):
                self.buttons_text[i][x].set('')
