from launcher_handler import *

import tkinter.font as font
import tkinter.ttk as ttk
from tkinter import *
import logging

def tab_changelog_window(parent):
    log_message(logging.INFO, "Setup: Initialised changelog window")

    changelog_1 = Frame(parent)
    changelog_1.pack()
    Label(changelog_1, text="TerrariaPYLauncher v0.1 Developer Demo", fg="black", font=font.Font(size=10, weight="bold")).grid(column=0, row=0, sticky=N)
    Label(changelog_1, text="+ Implemented Changelog tab\n+ Implemented settings tab\n+ Added support for downloading versions", fg="black", font=font.Font(size=10)).grid(column=0, row=1, sticky=N)

    changelog_0 = Frame(parent)
    changelog_0.pack()
    Label(changelog_0, text="TerrariaPYLauncher Preview", fg="black", font=font.Font(size=10, weight="bold")).grid(column=0, row=0, sticky=N)
    Label(changelog_0, text="This launcher is purely a concept, don't immediately expect everything to work.\nAlso, ensure you backup your data", fg="black", font=font.Font(size=10)).grid(column=0, row=1, sticky=N)