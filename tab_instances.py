from launcher_handler import *

from tkscrolledframe import ScrolledFrame
from tktooltip import ToolTip
import tkinter.ttk as ttk
from tkinter import *
import logging

def identify_button(button_id):
    log_message(logging.WARNING, f"Instance Manager: instance {button_id} clicked")

def add_instance(parent, instance_id):
    selected = False
    if instance_id == 3202211: selected = True

    highlight_colour = "black"
    highlight_thickness = 1
    if selected:
        highlight_colour = "red"
        highlight_thickness = 3

    instance_frame = Frame(parent, highlightbackground=highlight_colour, highlightthickness=highlight_thickness)
    instance_frame.pack(padx=160, pady=5)

    left_frame = Frame(instance_frame, highlightthickness=0)
    left_frame.grid(column=0, row=0)

    Button(instance_frame, text=f"icon", state="disabled", relief=GROOVE, width=7, height=3).grid(column=0, row=0, padx=2, pady=2, sticky=W)

    Label(instance_frame, text=f"ID: instance_{instance_id}\n", fg="#D0D0D0").grid(column=3, row=0, sticky=NE)

    button = ttk.Button(instance_frame, text="Select Instance", width=14, command=lambda id=instance_id: identify_button(id))
    button.grid(column=3, row=0, sticky=SE)
    ToolTip(button, msg="Switch to the selected version", delay=1)

    if selected:
        button.config(state="disabled", text="Selected")

    Label(instance_frame, text="").grid(column=2, row=0, padx=100)
    Label(left_frame, text="default_instance\n1.0.6.1").grid(column=1, row=0, padx=63)
    Label(left_frame, text="2022-1-1", fg="#8E8E8E").grid(column=1, row=1)

def tab_instances_window(parent):
    log_message(logging.INFO, "Setup: Initialised instances window")

    scrollable = ScrolledFrame(parent, scrollbars="vertical", relief=FLAT)
    scrollable.pack(side="top", expand=1, fill="both")
    main_frame = scrollable.display_widget(Frame)

    Label(main_frame, text="").pack()
    
    for x in range(1,25):
        instance_id = int(f"{x}202211")
        add_instance(main_frame, instance_id)

    Label(main_frame, text="").pack()