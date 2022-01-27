import tkinter as tk
from tkinter import filedialog

def ask_file(check_cancel=True):
    return __popup(filedialog.askopenfilename, check_cancel)

def ask_folder(check_cancel=True):
    return __popup(filedialog.askdirectory, check_cancel)

def __popup(func, check_cancel):
    root = tk.Tk()
    root.withdraw()

    _dir = func()
    if check_cancel:
        if _dir == '':
            print('[Warning] Popup menu is canceled.')

    return _dir
