from threading import Thread
import tkinter.font as font
import tkinter.ttk as ttk
from requests import get
from json import load
from tkinter import *
import logging

def log_message(level, message):
    logging.basicConfig(format='[%(asctime)s %(process)d %(levelname)s] %(message)s')
    logging.getLogger().setLevel(logging.INFO)
    logging.log(level, message)

def get_versions():
    versions = []
    data = load(open("./launcher.json"))
    for version in data["versions"]:
        versions.append(version)

    reversed_versions = [entry for entry in reversed(versions)]
    return reversed_versions

def error_window(parent, error, description):
    def error_window_exit(window):
        log_message(logging.WARNING, "Error dismissed")
        window.destroy()
        window.update()

    log_message(logging.ERROR, error)

    window = Toplevel(parent)
    window.geometry("200x100")
    window.title("Error!")
    window.iconbitmap("./favicon.ico")
    window.resizable(False, False)

    Label(window, text=f"Error: {error.title()}!\n", fg="red", font=font.Font(size=10, weight="bold")).pack()
    Label(window, text=f"{description}\n", fg="black").pack()
    ttk.Button(window, text="Dismiss", width=14, command=lambda: error_window_exit(window)).pack()

def download_window(parent, version):
    def download_window_exit(window):
        log_message(logging.INFO, "Download completed")
        window.destroy()
        window.update()

    log_message(logging.INFO, "Download started")

    window = Toplevel(parent)
    window.geometry("225x100")
    window.title("0% Done")
    window.iconbitmap("./favicon.ico")
    window.resizable(False, False)

    title = Label(window, text=f"Downloading Terraria {version}...", font=font.Font(size=10, weight="bold"))
    title.pack()
    progressbar = ttk.Progressbar(window, orient=HORIZONTAL, length=180)
    progressbar.pack(padx=5, pady=15)
    button = ttk.Button(window, text="Cancel", width=14, command=lambda: download_window_exit(window))
    button.pack()

    Thread(target=download_version, args=(window, version, title, progressbar, button)).start()

def download_version(window, version, title, progressbar, button):
    def close_program():
        window.destroy()
        
    def disable_event():
        log_message(logging.WARNING, "Discarded WM_DELETE_WINDOW protocol")
        pass

    try:
        window.protocol("WM_DELETE_WINDOW", disable_event)
        button.config(state="disabled")
        with open(f"./versions/{version}.zip", 'wb') as f:
            response = get(f"https://archive.org/download/Terraria-DE-Archive/{version[0:3]}/{version}.zip", stream=True)
            total = response.headers.get('content-length')

            if total is None:
                f.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                    downloaded += len(data)
                    f.write(data)
                    done = int(100*downloaded/total)
                    progressbar['value'] = done
                    log_message(logging.INFO, f"Download progress: {done}%")
                    window.title(f"{done}% Done")
                    if done == 100:
                        window.title("Complete")
                        button.config(text="Done")
    except:
        log_message(logging.ERROR, f"Download failed")
        window.title("Failed")
        title.config(text="Download Failed!", fg="red")
        button.config(text="Cancel")
        
    window.protocol("WM_DELETE_WINDOW", close_program)
    button.config(state="normal")