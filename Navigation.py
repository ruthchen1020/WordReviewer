import customtkinter as ctk


class Navigation(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # Set the grid layout as 5x1
        self.grid_rowconfigure(index=4, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        # Create widgets
        self.navigation_label = ctk.CTkLabel(
            master=self
            , text='Word Reviewer'
            , font=ctk.CTkFont(size=15, weight='bold')
        )
        self.test_review_button = ctk.CTkButton(
            master=self
            , height=40
            , border_spacing=10
            , fg_color='transparent'
            , hover_color=('gray70', 'gray30')
            , text_color=('gray10', 'gray90') 
            , text='Test Review'
            , command=self.test_review_button_event
            , anchor='w'
        )
        self.category_review_button = ctk.CTkButton(
            master=self
            , height=40
            , border_spacing=10
            , fg_color='transparent'
            , hover_color=('gray70', 'gray30')
            , text_color=('gray10', 'gray90')
            , text='Category Review'
            , command=self.category_review_button_event
            , anchor='w'
        )
        self.google_translate_button = ctk.CTkButton(
            master=self
            , height=40
            , border_spacing=10
            , fg_color='transparent'
            , hover_color=('gray70', 'gray30')
            , text_color=('gray10', 'gray90')
            , text='Google Translate'
            , command=self.google_translate_button_event
            , anchor='w'
        )
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            master=self
            , values=['System', 'Light', 'Dark']
            , command=self.appearance_mode_menu_event)

        self.set_widgets_location()


    def test_review_button_event(self):
        self.select_frame_by_name(name='tr')


    def category_review_button_event(self):
        self.select_frame_by_name(name='cr')


    def google_translate_button_event(self):
        self.select_frame_by_name(name='gt')


    def select_frame_by_name(self, name):
        # Set button color for the selected button
        self.test_review_button.configure(
            fg_color=('gray75', 'gray25') if name == 'tr' else 'transparent'
        )
        self.category_review_button.configure(
            fg_color=('gray75', 'gray25') if name == 'cr' else 'transparent'
        )
        self.google_translate_button.configure(
            fg_color=('gray75', 'gray25') if name == 'gt' else 'transparent'
        )

        # Show the selected frame
        if name == 'tr':
            self.parent.test_review_frame.grid(column=1, row=0, sticky=ctk.NSEW)
        else:
            self.parent.test_review_frame.grid_forget()
        if name == 'cr':
            self.parent.category_review_frame.grid(
                column=1
                , row=0
                , sticky=ctk.NSEW
            )
        else:
            self.parent.category_review_frame.grid_forget()
        if name == 'gt':
            self.parent.google_translate_frame.grid(
                column=1
                , row=0
                , sticky=ctk.NSEW
            )
        else:
            self.parent.google_translate_frame.grid_forget()


    def appearance_mode_menu_event(self, new_appearance_mode):
        ctk.set_appearance_mode(mode_string=new_appearance_mode)


    def set_widgets_location(self):
        self.navigation_label.grid(column=0, padx=20, pady=20, row=0)
        self.test_review_button.grid(column=0, row=1, sticky=ctk.EW)
        self.category_review_button.grid(column=0, row=2, sticky=ctk.EW)
        self.google_translate_button.grid(column=0, row=3, sticky=ctk.EW)
        self.appearance_mode_menu.grid(
            column=0
            , padx=20
            , pady=20
            , row=6
            , sticky=ctk.S
        )
