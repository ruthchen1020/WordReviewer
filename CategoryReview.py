import customtkinter as ctk
import tkinter as tk

from utils import save_note, set_note
from WordScrollableFrame import WordScrollableFrame


class CategoryReview(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # Set grid layout
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Needed attributes
        self.current_dict = tk.StringVar()
        self.current_word = tk.StringVar()
        self.current_sent = tk.StringVar()
        self._dict_words = None
        self._dict_sents = None

        # Set default values
        self.current_dict.set('l1')

        # word_scrollable_frame
        self.words_scrollable_frame = WordScrollableFrame(
            self
            , command=self.update_page
            , width=150
        )

        for word in self.parent.data[self.current_dict.get()].keys():
            self.words_scrollable_frame.add_item(word)

        # sentence_frame
        self.sentence_frame = ctk.CTkFrame(self, width=370)
        self.sentence_frame.grid_rowconfigure(0, weight=1)
        self.sentence_frame.grid_rowconfigure(1, weight=1)
        self.sentence_frame.grid_columnconfigure(0, weight=1)
        self.sentence_title_label = ctk.CTkLabel(
            self.sentence_frame
            , text='Sentence'
            , font=ctk.CTkFont(size=15, weight='bold')
        )
        self.sentence_label = ctk.CTkLabel(
            self.sentence_frame
            , textvariable=self.current_sent
        )

        # note_frame
        self.note_frame = ctk.CTkFrame(self, width=370)
        self.note_frame.grid_rowconfigure(0, weight=1)
        self.note_frame.grid_rowconfigure(1, weight=4)
        self.note_frame.grid_columnconfigure(0, weight=1)
        self.note_title_label = ctk.CTkLabel(
            self.note_frame
            , text='Note'
            , font=ctk.CTkFont(size=15, weight='bold')
        )
        self.note = ctk.CTkTextbox(self.note_frame, width=350)

        # functions_frame
        self.functions_frame = ctk.CTkFrame(self, width=550)
        self.functions_frame.grid_columnconfigure(0, weight=1)
        self.functions_frame.grid_columnconfigure(1, weight=1)
        self.dict_menu = ctk.CTkOptionMenu(
            self.functions_frame
            , variable=self.current_dict
            , values=parent.dict_names
            , command=self.change_dict)
        self.save_button = ctk.CTkButton(
            self.functions_frame
            , text='Save'
            , command=self.save_button_event)

        self.change_dict()
        self.set_widgets_location()


    def update_page(self, current_word_str=None):
        if current_word_str is None:
            self.current_word.set('')
            self.current_sent.set('')
            set_note(self, clear=True)

            return

        self.current_word.set(current_word_str)

        for button in self.words_scrollable_frame.button_list:
            if button.cget('text') == current_word_str:
                button.configure(
                    fg_color=('gray75', 'gray25')
                )
            else:
                button.configure(
                    fg_color='transparent'
                )

        cwi_int = self._dict_words.index(current_word_str)
        self.current_sent.set(self._dict_sents[cwi_int])

        set_note(self)


    def save_button_event(self):
        save_note(self)


    def change_dict(self, *args):
        self._dict_words = list(
            self.parent.dicts[self.current_dict.get()].keys()
        )
        self._dict_sents = list(
            self.parent.dicts[self.current_dict.get()].values()
        )

        self.words_scrollable_frame.remove_all_items()

        for word in self._dict_words:
            self.words_scrollable_frame.add_item(word)

        self.update_page()


    def set_widgets_location(self):
        # words_scrollable_frame
        self.words_scrollable_frame.grid(
            row=1
            , column=0
            , padx=(20, 10)
            , pady=10
            , sticky=ctk.NSEW
        )

        # sentence_frame
        self.sentence_frame.grid(
            row=0
            , column=0
            , padx=20
            , pady=10
            , columnspan=2
            , sticky=ctk.NSEW
        )
        self.sentence_title_label.grid(
            row=0
            , column=0
            , padx=10
            , pady=(10, 0)
        )
        self.sentence_label.grid(
            row=1
            , column=0
            , padx=10
            , pady=(0, 10)
        )

        # note_frame
        self.note_frame.grid(
            row=1
            , column=1
            , padx=(10, 20)
            , pady=10
            , sticky=ctk.NSEW
        )
        self.note_title_label.grid(
            row=0
            , column=0
            , padx=10
            , pady=(10, 5)
        )
        self.note.grid(
            row=1
            , column=0
            , padx=10
            , pady=(5, 10)
        )

        # functions_frame
        self.functions_frame.grid(
            row=2
            , column=0
            , padx=20
            , pady=(10, 20)
            , columnspan=2
            , sticky=ctk.NSEW
        )
        self.dict_menu.grid(
            row=0
            , column=0
            , padx=10
            , pady=10
        )
        self.save_button.grid(
            row=0
            , column=1
            , padx=10
            , pady=10
        )