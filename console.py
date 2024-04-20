from tkinter import *
from tkinter import scrolledtext
from os import path
import subprocess
from py3d import IUI

folder = path.dirname(__file__)
bash = ">>> "
shell = False
vault = False
do = False
ask = False

def s_return(a):
    send_()

def send_():
    echo(in_.get(), True)
    exe(in_.get())

def echo(txt, bash_ = False):
    if bash_:
        out.insert(END, bash + txt + "\n")
    else:
        out.insert(END, txt + "\n")

# def menu(): subprocess.call("python " + '"' + folder + "\menu.py" + '"', shell=True)
# def game(): subprocess.call("python " + '"' +folder + "\game.py" + '"', shell=True)
# def vault_gtk(): subprocess.call("python " + '"' + folder + "\\vault-gtk.py" + '"', shell=True)

def exe(com: str):
    """executing command (com) in console window"""
    global bash, shell
    if not shell:
        if com[:4] == "echo":
            echo(com[5:])
    
        elif com == "quit" or com == "exit":
            try: exit()
            except: quit()
    
        elif com[:4] == "bash":
            bash = com[5:]
            echo("new bash:" + bash)

        elif com == "shell" or com == "cmd":
            bash = "cmd: "
            echo("now commands will be redirected to cmd.exe with bash:\n" + '\t"' + bash + '"')
            echo("to escape use 'exit'")
            shell = True

        elif com[:4] == "help":
            if com == "help":
                show_coms()
            else:
                get_help(com[5:])

        elif com == "anim":
            IUI().anim()

        elif com == "clear":
            clear_()

        else:
            echo("ERROR: command " + com + " are not existing or can not be used")

    elif shell:
        if com == "exit":
            echo("exiting cmd...")
            bash = ">>> "
            shell = False
        else:
            echo(subprocess.getoutput(com, encoding="cp866"))
            # except: echo("ERROR: command are not existing or can not be used")

def clear_():
    out.delete(1.0, END)

def show_coms():
    echo("list of available commands:")
    echo("\techo")
    echo("\tquit")
    echo("\tbash")
    echo("\tanim")
    echo("\tshell or cmd")
    echo("\tclear")

def get_help(com):
    if com == "echo":
        echo("prints value after 'echo' in console")
    
    elif com == "quit":
        echo("exit console")
    
    elif com == "bash":
        echo("changing default bash '>>> ' to bash, typed after 'bash'")

    elif com == "shell" or com == "cmd":
        echo("redirect commands to cmd.exe with bash 'cmd: '")
        echo("to stop use exit command")

    elif com == "clear":
        echo("clearing console")

    else:
        echo("unknown command")

cmd = Tk()
cmd.geometry("500x354")
cmd.title("Console")

out = scrolledtext.ScrolledText(cmd, width=59, height=20)
out.place(x=0, y=0)

in_ = Entry(cmd, width=59)
in_.place(x=0, y=330)
in_.focus()

send = Button(cmd, text="Send" , command=send_)
send.place(x=360, y=328)

clear = Button(cmd, text="Clear all", command=clear_)
clear.place(x=402, y=328)

ext = Button(cmd, text="QUIT", command=quit)
ext.place(x=460, y=328)

cmd.bind("<Return>", s_return)

cmd.mainloop()