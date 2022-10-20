from launcher_handler import *
from game_manager import *

from tktooltip import ToolTip
import tkinter.ttk as ttk
from tkinter import *
import logging

def tab_settings_window(parent):
    log_message(logging.INFO, "Setup: Initialised settings window")

    versions = get_versions()
    selected_version = StringVar()
    install_directory = StringVar()
    save_directory = StringVar()

    install_directory.set("{install_directory}")
    save_directory.set("{save_directory}")

    # game settings
    game_settings = LabelFrame(parent, text="Instance Settings")
    game_settings.pack(padx=10, pady=24)

    download_option_menu = Frame(game_settings)
    download_option_menu.grid(column=0, row=0, padx=5)

    option_menu = Frame(download_option_menu, highlightbackground="black", highlightthickness=1)
    option_menu.grid(column=1, row=0, padx=5)

    Label(download_option_menu, text="Version:", fg="black").grid(column=0, row=0, pady=5)
    ttk.OptionMenu(option_menu, selected_version, versions[0], *versions, style="TMenubutton", direction="below").pack()
    
    Label(game_settings, text="").grid(column=1, row=0, padx=250)
    install_version_button = ttk.Button(game_settings, text=f"Install version", width=20, command=lambda: download_window(parent, selected_version.get()))
    install_version_button.grid(column=2, row=0, padx=3)
    ToolTip(install_version_button, msg="Download and install the selected version", delay=1)

    # install settings
    install_settings = LabelFrame(parent, text="Install configuration")
    install_settings.pack(padx=10, pady=0)

    location_menu = Frame(install_settings)
    location_menu.grid(column=0, row=0)

    Label(location_menu, text="Terraria install location:", fg="black").grid(column=0, row=0)
    ttk.Entry(location_menu, textvariable=install_directory, width=48).grid(column=1, row=0, padx=5)

    Label(location_menu, text="Terraria save location:", fg="black").grid(column=0, row=1, pady=5)
    ttk.Entry(location_menu, textvariable=save_directory, width=48).grid(column=1, row=1, padx=5)

    Label(location_menu, text="").grid(column=3, row=1, padx=115)
    update_locations_button = ttk.Button(location_menu, text=f"Update Locations", width=20)
    update_locations_button.grid(column=4, row=1, padx=3)
    ToolTip(update_locations_button, msg="Update Terraria's install and save locations", delay=1)
