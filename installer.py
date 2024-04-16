import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from threading import Thread
from time import sleep as wait
from shutil import copy

step = 0
fold = os.path.dirname(__file__)

def main():
    global step
    while 1:
        if step == 0:
            lbl_select.place(x=150, y=10)
            lbl_path.place(x=5, y=70)
            btn_ch.place(x=170, y=30)
            btn_next.place(x=345, y=100)

        elif step == 1:
            btn_ch.destroy()
            lbl_select.destroy()
            lbl_path.destroy()
            btn_next.destroy()
            bar.place(x=50, y=50)
            lbl_load.place(x=160, y=30)
            thd_load = Thread(target=loading)
            break

        elif step == 2:
            bar.destroy()
            lbl_load.destroy()

            lbl_finish.place(x=5, y=30)
            btn_finish.place(x=160, y=100)

    
    thd_load.start()

def loading():
    global step
    k = 0
    while k < 100:
        bar['value'] = k
        if k == 75:
            try:
                copy(os.path.dirname(__file__) + r"\py3d.py", fold)
            except:
                messagebox.showerror("File copy error", "Destination file are similar as source file. \nPlease close installation programm")
                exit()

        win.title("py3d installer (installing " + "[" + "#" * int(k / 19) + "])")
        wait(0.1)
        k += 1
    
    win.title("py3d installer")
    wait(3)
    step = 2
    main()

def folder():
    global fold
    fold = filedialog.askdirectory(initialdir=os.path.dirname(__file__))
    lbl_path.configure(text="Current folder: " + fold)

def next():
    global step
    step += 1


win = Tk()
win.title("py3d installer")
win.geometry("400x130")

lbl_select = Label(win, text="Select python Lib path:")
lbl_path = Label(win, text="Current folder: " + fold)
lbl_load = Label(win, text="Installing...")
lbl_finish = Label(win, text="You successfully installed py3d to " + fold)
btn_ch = Button(text="Choose folder", command=folder)
btn_next = Button(text="Next ->", command=next)
btn_finish = Button(text="Finish", command=exit)
bar = Progressbar(win, length=300)

thd_main = Thread(target=main)
thd_main.start()

win.mainloop()