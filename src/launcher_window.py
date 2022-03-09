from random import randint
import tkinter.ttk as ttk
from tkinter import *

def main_window(launcher_version: str, versions):
    global root
    global log_text
    global clicked
    global style

    root = Tk()
    root.geometry("854x491")
    root.title(f"Terraria Launcher v{launcher_version}")
    root.config(bg="#292929")
    root.iconbitmap("./resources/favicon.ico")
    root.resizable(False, False)

    clicked = StringVar()

    style=ttk.Style()
    style.configure("TMenubutton", width=10)
    
    img = PhotoImage(file=f"./resources/backgrounds/bg{randint(0,3)}.png")
    Label(root, image=img, highlightthickness=0, bd=0).grid(column=0, row=1)

    #version selection setup
    version_selection = Frame(root)
    version_selection.config(bg="#292929", pady=5, padx=5)
    version_selection.grid(column=0, row=0, sticky=NE)

    Label(version_selection, text="Version:", fg="white", bg="#292929").grid(column=0, row=0)
    ttk.OptionMenu(version_selection, clicked, versions[0], *versions, style="TMenubutton", direction="below").grid(column=1, row=0)

    #button toolbar setup
    toolbar_buttons = Frame(root)
    toolbar_buttons.config(bg="#292929", pady=5)
    toolbar_buttons.grid(column=0, row=2, sticky=S)

    ttk.Button(toolbar_buttons, text="Change Version", width=14).grid(column=1, row=0)
    ttk.Button(toolbar_buttons, text="Instances", width=14).grid(column=2, row=0)
    ttk.Button(toolbar_buttons, text="Backup Data", width=14).grid(column=3, row=0)
    ttk.Button(toolbar_buttons, text="Launch Game", width=14).grid(column=4, row=0)

    #status log setup
    log_text = Label(root, text="Status logs will appear in place of this text!", fg="red", bg="#292929").grid(column=0, row=0, sticky=NW, padx=5, pady=5)

    #current version setup
    instance_text = Label(root, text=f"{versions[0]} | {{Instance name here}}", fg="white", bg="#292929").grid(column=0, row=2, sticky=SW, padx=5, pady=5)

    root.mainloop()