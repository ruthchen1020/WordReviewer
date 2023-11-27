import customtkinter as ctk
import json
import os


from TestReview import TestReview
from CategoryReview import CategoryReview


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Word Reviewer")
        self.geometry("800x450")
        self.resizable(width=0, height=0)

        self.dicts = {}
        self.dict_names = ['l1','l2']
        self.create_dict()

        self.initialize_data()

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Word Reviewer", compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.trButton = ctk.CTkButton(
            self.navigation_frame
            , corner_radius=0
            , height=40
            , border_spacing=10
            , text="Test Review"
            ,fg_color="transparent"
            , text_color=("gray10", "gray90")
            , hover_color=("gray70", "gray30")
            , anchor="w"
            , command=self.trButton_event)
        self.trButton.grid(row=1, column=0, sticky="ew")

        self.crButton = ctk.CTkButton(
            self.navigation_frame
            , corner_radius=0
            , height=40
            , border_spacing=10
            , text="Category Review"
            , fg_color="transparent"
            , text_color=("gray10", "gray90")
            , hover_color=("gray70", "gray30")
            , anchor="w"
            , command=self.crButton_event)
        self.crButton.grid(row=2, column=0, sticky="ew")

        self.gtButton = ctk.CTkButton(
            self.navigation_frame
            , corner_radius=0
            , height=40
            , border_spacing=10
            , text="Google Translate"
            , fg_color="transparent"
            , text_color=("gray10", "gray90")
            , hover_color=("gray70", "gray30")
            ,anchor="w"
            , command=self.gtButton_event)
        self.gtButton.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.navigation_frame
            , values=["System", "Light", "Dark"]
            , command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(
            row=6
            , column=0
            , padx=20
            , pady=20
            , sticky="s")

        # create home frame
        self.trFrame = TestReview(self)

        self.crFrame = CategoryReview(self)

        self.gtFrame = ctk.CTkFrame(
            self
            , corner_radius=0
            , fg_color="transparent"
        )


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.trButton.configure(
            fg_color=("gray75", "gray25") if name == "tr" else "transparent"
        )
        self.crButton.configure(
            fg_color=("gray75", "gray25") if name == "cr" else "transparent"
        )
        self.gtButton.configure(
            fg_color=("gray75", "gray25") if name == "gt" else "transparent"
        )

        # show selected frame
        if name == "tr":
            self.trFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.trFrame.grid_forget()
        if name == "cr":
            self.crFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.crFrame.grid_forget()
        if name == "gt":
            self.gtFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gtFrame.grid_forget()


    def trButton_event(self):
        self.select_frame_by_name("tr")


    def crButton_event(self):
        self.select_frame_by_name("cr")


    def gtButton_event(self):
        self.select_frame_by_name("gt")


    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


    def create_dict(self):
        for dict_name in self.dict_names:
            with open(
                    file='data/'+dict_name+'_words.txt'
                    , mode='r'
                    , encoding='UTF-8') as file:
                lines = file.read()
                words_list = lines.split('\n')

                file.close()

            with open(
                    file='data/'+dict_name+'_sentences.txt'
                    , mode='r'
                    , encoding='UTF-8') as file:
                lines = file.read()
                sentences_list = lines.split('\n')

            self.dicts[dict_name] = {}
            for i in range(len(words_list)):
                self.dicts[dict_name][words_list[i]] = sentences_list[i]


    def initialize_data(self):
        self.data = {}

        if not os.path.exists(path='data.json'):
            for dict_name in self.dict_names:
                self.data[dict_name] = {}

                for word, sentence in self.dicts[dict_name].items():
                    self.data[dict_name][word] = {
                        'sentence': sentence
                        , 'note': ''
                    }

            with open(file='data.json', mode='w', encoding='UTF-8') as file:
                json.dump(self.data, file)
                file.close()
        else:
            with open(file='data.json', mode='r', encoding='UTF-8') as file:
                self.data = json.load(file)
                file.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()
