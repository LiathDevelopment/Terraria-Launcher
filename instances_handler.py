from launcher_handler import *

from configparser import RawConfigParser
from os import mkdir, path, listdir
from tktooltip import ToolTip
from random import randint
import tkinter.ttk as ttk
from tkinter import *
import logging

def create_instance_window(parent):
    def kill_window():
        window.destroy()
        window.update()
    
    window = Toplevel(parent)
    window.geometry("259x95")
    window.title("New Instance")
    window.iconbitmap("./favicon.ico")
    window.resizable(False, False)

    instance_name = StringVar()

    Label(window, text="Instance Name:", fg="black").pack(side=TOP, anchor=NW, padx=10, pady=5)
    entry = ttk.Entry(window, textvariable=instance_name)
    entry.pack(padx=10, fill=X)

    buttons = Frame(window)
    buttons.config(pady=10)
    buttons.pack()

    ok_button = ttk.Button(buttons, text="Ok", width=14, command=lambda: create_profile(parent, window, buttons, instance_name))
    ok_button.grid(column=0, row=0, padx=5)
    ToolTip(ok_button, msg="Create Instance", delay=1)
    ttk.Button(buttons, text="Cancel", width=14, command=kill_window).grid(column=1, row=0, padx=5)

def check_folder_created():
    if path.isdir("./instances/") == False:
        mkdir("./instances")
        log_message(logging.INFO, "Instances folder created")
    else:
        log_message(logging.INFO, "Instances folder located")

def load_instance(instance):
    config = RawConfigParser()
    config.read(f"./instances/{instance}/Terraria/instance.properties")
    launcher_config = dict(config.items("INSTANCE_PROPERTIES"))
    return [instance, launcher_config]

def create_profile(parent, window, frame, instance_name):
    check_folder_created()
    if len(instance_name.get()) > 0 and instance_name.get() not in listdir("./instances/"):
        try:
            mkdir(f"./instances/{instance_name.get()}")
            mkdir(f"./instances/{instance_name.get()}/Terraria")
            f = open(f"./instances/{instance_name.get()}/Terraria/instance.properties", "x")
            f.write(f"[INSTANCE_PROPERTIES]\n# If this file is altered or deleted, the instance will break\n\nINSTANCE_ID={randint(1000000, 9999999)}\nVERSION=1.0.6.1\nLAST_USED=2022-1-1")
            f.close()
            log_message(logging.INFO, f"Instance {instance_name.get()} created.")
            frame.destroy()
            frame.update()
            window.destroy()
        except:
            error_window(window, "Instance Failed", "Perhaps try again?")
    else:
        error_window(window, "Instance Failed", "Is name already used?")