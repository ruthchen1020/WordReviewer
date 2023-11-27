import tkinter as tk


class GoogleTranslate(tk.Frame):
    def __init__(self, parent, controller):


# TODO
def interface3(self):
    '''頁面三'''
    frame2=WebView2(self.root,700,400)
    frame2.pack(side='left',padx=20)
    frame2.load_url('https://translate.google.com.tw/?hl=zh-TW')