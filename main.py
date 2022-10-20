from instances_handler import *
from launcher_handler import *
from game_manager import *
from tab_changelog import *
from tab_instances import *
from tab_output import *
from tab_settings import *

from tktooltip import ToolTip
import tkinter.ttk as ttk
from tkinter import *
import logging

def main_setup():
    def tab_changed(event):
        if tab_control.index(tab_control.select()) == 1:
            create_instance_button.grid(column=0, row=0, pady=10, sticky=N)
            launch_game_button.grid_remove()
            for widgets in tab_instances.winfo_children():
                widgets.destroy()
            log_message(logging.INFO, "Setup: Destroyed tab_instances children")
            tab_instances_window(tab_instances)
        else:
            create_instance_button.grid_remove()
            launch_game_button.grid(column=0, row=0, pady=10, sticky=N)

    log_message(logging.WARNING, "This launcher is still in the concept demo stage of development")
    
    root = Tk()
    root.geometry("854x480")
    root.title("TerrariaPYLauncher v0.1 | Developer Demo 1")
    root.iconbitmap("./favicon.ico")
    root.config(bg="#292929")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TMenubutton", width=10)

    tab_control = ttk.Notebook(root)
    root.bind("<<NotebookTabChanged>>", tab_changed)

    tab_changelog = ttk.Frame(tab_control)
    tab_instances = ttk.Frame(tab_control)
    tab_settings = ttk.Frame(tab_control)
    tab_output = ttk.Frame(tab_control)
    tab_about = ttk.Frame(tab_control)

    tab_control.add(tab_changelog, text="Changelog")
    tab_control.add(tab_instances, text="Instances")
    tab_control.add(tab_settings, text="Settings")
    #tab_control.add(tab_output, text="Output")
    tab_control.add(tab_about, text="About")
    tab_control.pack(expand=1, fill="both")

    toolbar_frame = Frame(root, bg="#292929")
    toolbar_frame.pack(side=BOTTOM)

    launch_game_button = ttk.Button(toolbar_frame, text="Launch Game", width=14, command=lambda: launch_game(root))
    launch_game_button.grid(column=0, row=0, pady=10, sticky=N)
    ToolTip(launch_game_button, msg="Launch Terraria", delay=1)

    create_instance_button = ttk.Button(toolbar_frame, text="Create Instance", width=14, command=lambda: create_instance_window(root))
    create_instance_button.grid(column=1, row=0, pady=10, sticky=N)
    ToolTip(create_instance_button, msg="Create a new Instance", delay=1)

    #Label(toolbar_frame, text="This is a beta concept, some features may be unstable or not yet implemented into the launcher. You should backup your data.", fg="red", bg="#292929").grid(column=0, row=0)
    
    #tab_output_window(tab_output)
    tab_settings_window(tab_settings)
    tab_instances_window(tab_instances)
    tab_changelog_window(tab_changelog)

    log_message(logging.INFO, "Setup: Finished intialising children windows")
    
    root.mainloop()

main_setup()