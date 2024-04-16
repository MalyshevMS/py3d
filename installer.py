import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from threading import Thread
from time import sleep as wait

step = 0

def main():
    global step
    while 1:
        if step == 0:
            lbl_select.grid(column=0, row=0)
            btn_ch.grid(column=0, row=1)
            btn_next.place(x=345, y=220)
            btn_prev.place(x=5, y=220)

        elif step == 1:
            btn_ch.destroy()
            lbl_select.destroy()
            bar.grid(column=0, row=0)

def folder():
    global fold
    fold = filedialog.askdirectory(initialdir=os.path.dirname(__file__))

def next():
    global step
    step += 1

def previos():
    global step
    step -= 1

win = Tk()
win.title("py3d installer")
win.geometry("400x250")

lbl_select = Label(win, text="Select python Lib path:")
btn_ch = Button(text="Choose folder", command=folder)
btn_next = Button(text="Next ->", command=next)
btn_prev = Button(text="<- Prev", command=previos)
bar = Progressbar(win, length=300)

a = Thread(target=main)
a.start()

os.__file__

win.mainloop()