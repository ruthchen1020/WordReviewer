import customtkinter as ctk


class WordScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.button_list = []


    def add_item(self, word_str):
        button = ctk.CTkButton(
            self
            , corner_radius=0
            , height=40
            , border_spacing=10
            , text=word_str
            , fg_color='transparent'
            , text_color=('gray10', 'gray90')
            , hover_color=('gray70', 'gray30')
            , anchor='w')

        if self.command is not None:
            button.configure(command=lambda: self.command(word_str))

        button.grid(
            row=len(self.button_list)
            , column=0
            , pady=(0, 10)
            , padx=5)

        self.button_list.append(button)


    # def remove_item(self, word_str):
    #     for button in self.button_list:
    #         if word_str == button.text:
    #             button.destroy()
    #             self.button_list.remove(button)
    #             return


    def remove_all_items(self):
        for button in self.button_list:
            button.destroy()
        
        self.button_list = []

        return