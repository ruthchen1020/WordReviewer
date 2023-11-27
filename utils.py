import tkinter as tk
import json


def save_note(frame):
    cd_str = frame.current_dict.get()
    cw_str = frame.current_word.get()

    if cw_str == '':
        return

    try:
        frame.parent.data[cd_str][cw_str]['note'] = \
            frame.note.get('1.0', tk.END)[:-1]
    except:
        frame.parent.data[cd_str][cw_str]['note'] = ''

    with open(file='data.json', mode='w', encoding='UTF-8') as file:
        json.dump(frame.parent.data, file)
        file.close()


def set_note(frame, clear=False):
    frame.note.delete('1.0', tk.END)

    if clear:
        return

    cd_str = frame.current_dict.get()
    cw_str = frame.current_word.get()

    try:
        note = frame.parent.data[cd_str][cw_str]['note']
    except:
        note = ''

    frame.note.insert('1.0', note)