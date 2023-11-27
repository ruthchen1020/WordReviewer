import customtkinter as ctk
from tkwebview2.tkwebview2 import WebView2


class GoogleTranslate(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # Set grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # browser frame
        self.webview = WebView2(self, width=100, height=100)
        self.webview.grid(row=0, column=0, sticky=ctk.NSEW)

        url = 'https://translate.google.com.tw/?hl=zh-TW'
        self.webview.load_url(url)
