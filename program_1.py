# Eliya Statema
# 4/8/25
# My Favorite Saying GUI

import tkinter

class QuoteGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("My Favorite Saying")
        self.label = tkinter.Label(self.main_window, text = '"What I say is that, if a \
fellow really likes potatoes,\n he must be a pretty decent sort of fellow."\n - A.A. Milne')
        self.label.pack(ipadx = 10, ipady = 10)
        tkinter.mainloop()

if __name__ == '__main__':
    quoteGUI = QuoteGUI()