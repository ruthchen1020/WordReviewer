import customtkinter as ctk
import tkinter as tk
import random

from utils import save_note, set_note


class TestReview(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # Set grid layout 
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Needed attributes
        self.current_word_index = tk.StringVar()
        self.all_words_num = tk.StringVar()
        self.current_dict = tk.StringVar()
        self.current_word = tk.StringVar()
        self.current_sent = tk.StringVar()
        self._dict_words = None
        self._dict_sents = None

        # question_frame
        self.question_frame = ctk.CTkFrame(self, width=370)
        self.question_frame.grid_rowconfigure(0, weight=1)
        self.question_frame.grid_rowconfigure(1, weight=1)
        self.question_frame.grid_columnconfigure(0, weight=1)
        
        self.question_index_info = tk.StringVar()
        self.question_index_info_label = ctk.CTkLabel(
            self.question_frame
            , textvariable=self.question_index_info
            , compound='left'
            , font=ctk.CTkFont(size=15, weight='bold')
        )
        self.question = tk.StringVar()
        self.question_label = ctk.CTkLabel(
            self.question_frame
            , textvariable=self.current_sent
        )

        # answer_options_frame
        self.answer_options_frame = ctk.CTkFrame(self, width=150)
        self.answer_options_frame.grid_rowconfigure(0, weight=1)
        self.answer_options_frame.grid_rowconfigure(1, weight=1)
        self.answer_options_frame.grid_rowconfigure(2, weight=1)
        self.answer_options_frame.grid_rowconfigure(3, weight=1)
        self.answer_options_frame.grid_columnconfigure(0, weight=1)
        self.answer_options = {
            '0': tk.StringVar()
            , '1': tk.StringVar()
            , '2': tk.StringVar()
            , '3': tk.StringVar()
        }
        related_obs_var = tk.IntVar()
        self.answer_option_buttons = {
            '0': ctk.CTkRadioButton(
                self.answer_options_frame
                , textvariable=self.answer_options['0']
                , variable=related_obs_var
                , value='0')
            , '1': ctk.CTkRadioButton(
                self.answer_options_frame
                , textvariable=self.answer_options['1']
                , variable=related_obs_var
                , value='1')
            , '2': ctk.CTkRadioButton(
                self.answer_options_frame
                , textvariable=self.answer_options['2']
                , variable=related_obs_var
                , value='2')
            , '3': ctk.CTkRadioButton(
                self.answer_options_frame
                , textvariable=self.answer_options['3']
                , variable=related_obs_var
                , value='3')
        }

        # answer_frame
        self.answer_frame = ctk.CTkFrame(self, width=150)
        self.answer_frame.grid_rowconfigure(0, weight=1)
        self.answer_frame.grid_columnconfigure(0, weight=1)
        self.answer_title_label = ctk.CTkLabel(
            self.answer_frame
            , text='Answer'
            , compound='left'
            , font=ctk.CTkFont(size=15, weight='bold')
        )
        self.answer_label = ctk.CTkLabel(
            self.answer_frame
        )

        # note_frame
        self.note_frame = ctk.CTkFrame(self, width=370)
        self.note_frame.grid_rowconfigure(0, weight=1)
        self.note_frame.grid_rowconfigure(1, weight=4)
        self.note_frame.grid_columnconfigure(0, weight=1)
        self.note_title_label = ctk.CTkLabel(
            self.note_frame
            , text='Note'
            , compound='left'
            , font=ctk.CTkFont(size=15, weight='bold')
        )
        self.note = ctk.CTkTextbox(self.note_frame, width=350)

        # functions_frame
        self.functions_frame = ctk.CTkFrame(self, width=550)
        self.functions_frame.grid_rowconfigure(0, weight=1)
        self.functions_frame.grid_columnconfigure(0, weight=1)
        self.functions_frame.grid_columnconfigure(1, weight=1)
        self.functions_frame.grid_columnconfigure(2, weight=1)
        self.dict_menu = ctk.CTkOptionMenu(
            self.functions_frame
            , variable=self.current_dict
            , values=parent.dict_names
            , command=self.change_dict
        )
        self.see_answer_button = ctk.CTkButton(
            self.functions_frame
            , text='See Answer'
            , command=self.see_answer_event
        )
        self.next_button = ctk.CTkButton(
            self.functions_frame
            , text='Next'
            , command=self.next_event
        )

        # Set default values
        self.current_dict.set('l1')
        self.answer_label.configure(text='')

        self.change_dict()
        self.set_widgets_location()


    def change_dict(self, *args):
        self._dict_words = list(
            self.parent.dicts[self.current_dict.get()].keys()
        )
        self._dict_sents = list(
            self.parent.dicts[self.current_dict.get()].values()
        )

        self.current_word_index.set('1')
        self.all_words_num.set(len(self._dict_words))

        cwi_int = (int(self.current_word_index.get()) - 1)
        
        self.current_word.set(self._dict_words[cwi_int])
        self.current_sent.set(
            self._dict_sents[cwi_int].split(self._dict_words[cwi_int])[0]
            + '_____'
            + self._dict_sents[cwi_int].split(self._dict_words[cwi_int])[1]
        )

        set_note(self)

        self.set_question_index_info()
        self.set_answer_options()
        self.answer_label.configure(text='')


    def set_question_index_info(self):
        self.question_index_info.set(
            self.current_word_index.get()
            + ' / '
            + self.all_words_num.get()
        )


    def set_answer_options(self):
        answer_index = random.randint(0, 3)
        cwi_int = (int(self.current_word_index.get()) - 1)
        used_word_ids = []

        for i in range(4):
            if i == answer_index:
                self.answer_options[str(i)].set(self._dict_words[cwi_int])
                used_word_ids.append(cwi_int)
                continue

            while True:
                word_id = random.randint(0, len(self._dict_words) - 1)

                if (word_id not in used_word_ids) and \
                        (word_id != cwi_int):
                    self.answer_options[str(i)].set(self._dict_words[word_id])
                    used_word_ids.append(word_id)
                    break


    def see_answer_event(self):
        self.answer_label.configure(text=self.current_word.get())


    def next_event(self):
        save_note(self)

        cwi_int = int(self.current_word_index.get())
        awn_int = int(self.all_words_num.get())

        if cwi_int < awn_int:
            self.current_word.set(self._dict_words[cwi_int])
            self.current_sent.set(
                self._dict_sents[cwi_int].split(self._dict_words[cwi_int])[0]
                + '_____'
                + self._dict_sents[cwi_int].split(self._dict_words[cwi_int])[1]
            )

            set_note(self)

            self.current_word_index.set(str(cwi_int + 1))
            self.set_question_index_info()
            self.set_answer_options()
            self.answer_label.configure(text='')


    def set_widgets_location(self):
        # question_frame
        self.question_frame.grid(
            row=0
            , column=0
            , padx=20
            , pady=10
            , columnspan=2
            , sticky=ctk.NSEW
        )
        self.question_index_info_label.grid(
            row=0
            , column=0
            , padx=10
            , pady=(10, 0)
            , columnspan=2
        )
        self.question_label.grid(
            row=1
            , column=0
            , padx=10
            , pady=(0, 10)
            , rowspan=2
            , columnspan=4
        )

        # answer_options_frame
        self.answer_options_frame.grid(
            row=1
            , column=0
            , padx=(20, 10)
            , pady=10
            , sticky=ctk.NSEW
        )
        for i in range(4):
            self.answer_option_buttons[str(i)].grid(
                row=i
                , column=0
                , padx=10
                , pady=5
                , sticky=ctk.W
            )

        # answer_frame
        self.answer_frame.grid(
            row=2
            , column=0
            , padx=(20, 10)
            , pady=10
            , sticky=ctk.NSEW
        )
        self.answer_title_label.grid(
            row=0
            , column=0
            , padx=10
            , pady=(10, 5)
        )
        self.answer_label.grid(
            row=1
            , column=0
            , padx=10
            , pady=(5, 10)
        )

        # note_frame
        self.note_frame.grid(
            row=1
            , column=1
            , padx=(10, 20)
            , pady=10
            , rowspan=2
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
            row=3
            , column=0
            , padx=20
            , pady=10
            , columnspan=2
            , sticky=ctk.NSEW
        )
        self.dict_menu.grid(
            row=0
            , column=0
            , padx=10
            , pady=10
        )
        self.see_answer_button.grid(
            row=0
            , column=1
            , padx=10
            , pady=10
        )
        self.next_button.grid(
            row=0
            , column=2
            , padx=10
            , pady=10
        )