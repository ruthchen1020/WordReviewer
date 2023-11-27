import customtkinter as ctk
import json
import os

from Navigation import Navigation
from TestReview import TestReview
from CategoryReview import CategoryReview
from GoogleTranslate import GoogleTranslate


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.title(string='Word Reviewer')
        self.geometry(geometry_string='800x450')
        self.resizable(width=False, height=False)

        # Set the grid layout as 1x2
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=1, weight=1)

        self.dicts = {}
        self.dict_names = ['l1','l2']

        # Load dicts from files
        self.load_dicts()

        # Initialize data.json file
        self.initialize_data()

        # Create frames
        self.navigation_frame = Navigation(self)
        self.test_review_frame = TestReview(self)
        self.category_review_frame = CategoryReview(self)
        self.google_translate_frame = GoogleTranslate(self)

        # Set the location of navigation_frame
        self.navigation_frame.grid(column=0, row=0, sticky=ctk.NSEW)


    def load_dicts(self):
        for dict_name in self.dict_names:
            with open(
                    file='data/'+dict_name+'_words.txt'
                    , mode='r'
                    , encoding='UTF-8') as file:
                lines = file.read()
                words_list = lines.split(sep='\n')

                file.close()

            with open(
                    file='data/'+dict_name+'_sentences.txt'
                    , mode='r'
                    , encoding='UTF-8') as file:
                lines = file.read()
                sentences_list = lines.split(sep='\n')

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
                json.dump(obj=self.data, fp=file)
                file.close()
        else:
            with open(file='data.json', mode='r', encoding='UTF-8') as file:
                self.data = json.load(fp=file)
                file.close()


if __name__ == '__main__':
    app = App()
    app.mainloop()
