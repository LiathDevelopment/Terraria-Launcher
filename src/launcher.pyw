import tkinter.ttk as ttk
from tkinter import *
from os import mkdir, path, listdir
from requests import get
from shutil import rmtree
from zipfile import ZipFile
from threading import Thread
from random import randint
from webbrowser import open as openURL
from shutil import move, copytree

archiveURL = "http://liath.xyz:81/Terraria/TerrariaArchive/"
terrariaDir = ""
versions = ["Alpha-Leak", "Beta-Leak", "1.0.0", "1.0.1", "1.0.2", "1.0.3", "1.0.4", "1.0.5", "1.0.6", "1.0.6.1", "1.1", "1.1.1", "1.1.2", "1.2", "1.2.0.1", "1.2.0.2", "1.2.0.3", "1.2.0.3.1-1", "1.2.0.3.1-2", "1.2.1", "1.2.1.1", "1.2.1.2-1", "1.2.1.2-2", "1.2.2", "1.2.3", "1.2.3.1-1", "1.2.3.1-2", "1.2.4", "1.2.4.1", "1.3.0.1", "1.3.0.2", "1.3.0.3", "1.3.0.4-1", "1.3.0.4-2", "1.3.0.5", "1.3.0.6", "1.3.0.7", "1.3.0.8", "1.3.1", "1.3.2", "1.3.2.1", "1.3.3", "1.3.3.1", "1.3.3.2", "1.3.3.3", "1.3.4", "1.3.4.1", "1.3.4.2", "1.3.4.3", "1.3.4.4", "1.3.5", "1.3.5.1", "1.3.5.2", "1.3.5.3", "1.4.0.1", "1.4.0.2", "1.4.0.3", "1.4.0.4", "1.4.0.5", "1.4.1", "1.4.1.1", "1.4.1.2", "1.4.2", "1.4.2.1", "1.4.2.2", "1.4.2.3"]

def version_switch():
    if "/steamapps/common/Terraria" not in terrariaDir:
        log.config(text="Invalid game directory, check configuration.")
        return
    if path.exists(f"./versions/{clicked.get()}.zip"):
        log.config(text="Version found, installing.")
        Thread(target=unzip_version).start()
    else:
        log.config(text="Version not found, downloading. This may take a little while.")
        Thread(target=download_version).start()

def download_version():
    try:
        r = get(f"http://liathdevelopment.org:81/resources/downloads/Terraria-Archive/{clicked.get()}.zip")
        with open(f"./versions/{clicked.get()}.zip",'wb') as output_file:
            output_file.write(r.content)
        log.config(text="Version downloaded from server.")
    except:
        log.config(text="Version download failed, failed to connect to server.")
        return

    log.config(text=f"Installing version {clicked.get()}.")
    Thread(target=unzip_version).start()

def unzip_version():
    try: rmtree(terrariaDir)
    except: pass
    try:
        mkdir(terrariaDir)
        with ZipFile(f"./versions/{clicked.get()}.zip", 'r') as zip:
            zip.extractall(terrariaDir)
        log.config(text=f"Version {clicked.get()} installed.")
    except:
        log.config(text="Version install failed, access was denied.")

def launch_game():
    try:
        openURL("steam://rungameid/105600")
    except:
        log.config(text="Failed to launch Terraria.")

def open_profiles():
    log.config(text="Profiles are still in beta testing.")
    profiles_window()

def profiles_window():
    global profilesWindow
    global profiles

    total_profiles = 0
    profilesWindow = Toplevel(root)
    # profilesWindow.geometry("265x345")
    profilesWindow.geometry("265x235")
    profilesWindow.title("Game Profiles")
    profilesWindow.iconbitmap("./icon.ico")
    profilesWindow.resizable(False, False)

    ttk.Button(profilesWindow, text="New Profile", command=create_profile_window).pack(fill=X, padx=5, pady=5)

    profiles = Listbox(profilesWindow, relief=GROOVE)

    for x in listdir("./profiles/"):
        total_profiles += 1
        profiles.insert(total_profiles, x)
    
    profiles.pack(fill=X, padx=5)

    ttk.Button(profilesWindow, text="Ok", command=switch_profile).pack(fill=X, padx=5, pady=5)

def create_profile():
    if len(profile_name_value.get()) > 0 and profile_name_value.get() not in listdir("./profiles/"):
        try:
            mkdir(f"./profiles/{profile_name_value.get()}")
            mkdir(f"./profiles/{profile_name_value.get()}/Terraria")
            f = open(f"./profiles/{profile_name_value.get()}/Terraria/profileid.txt", "x")
            f.write("# If this file is deleted this profile will become merged with the default profile\nprofile_id=" + profile_name_value.get())
            f.close()
            log.config(text=f"Profile {profile_name_value.get()} created.")
            create_profile_window_frame.destroy()
            create_profile_window_frame.update()
            profilesWindow.destroy()
            profilesWindow.update()
            profiles_window()
        except:
            log.config(text="Failed to create profile.")
    else:
        log.config(text="Failed to create profile.")

def switch_profile():
    active_profile = ""
    selected_profile_id = None

    if "My Games/Terraria" not in savesDir:
        log.config(text="Invalid save directory, check configuration.")
        return

    for i in profiles.curselection():
        selected_profile_id = profiles.get(i)
    if selected_profile_id is None:
        log.config(text="Failed to switch profile, no profile selected.")
    else:
        log.config(text=f"Switching profile to {selected_profile_id}.")
        if path.exists(f"./profiles/{selected_profile_id}"):
            log.config(text="Located profile folder.")
            try:
                f = open(savesDir + "/profileid.txt", "r")
                active_profile = f.readlines()[1].replace("profile_id=", "")
                f.close()
            except:
                active_profile = "(default profile)"
            if path.exists(f"./profiles/{active_profile}/") == False:
                mkdir(f"./profiles/{active_profile}")

            try:
                rmtree(f"./profiles/{active_profile}/")
                mkdir(f"./profiles/{active_profile}/Terraria/")
            except:
                pass

            try: move(savesDir, f"./profiles/{active_profile}/Terraria/")
            except: pass
            log.config(text="Moved active profile.")

            try: rmtree(savesDir)
            except: pass
            copytree(f"./profiles/{selected_profile_id}/Terraria/", savesDir)
            log.config(text=f"Active profile is now {selected_profile_id}.")
            update_active_profile()
            profilesWindow.destroy()
            profilesWindow.update()

        else:
            log.config(text="Failed to locate profile folder.")
            return

def update_active_profile():
    try:
        f = open(savesDir + "/profileid.txt", "r")
        active_profile = f.readlines()[1].replace("profile_id=", "")
        f.close()
    except:
        active_profile = "(default profile)"
    profileText.config(text=f"Active profile: {active_profile}")

def create_profile_window():
    global create_profile_window_frame
    global profile_name_value

    def killWindow():
        create_profile_window_frame.destroy()
        create_profile_window_frame.update()
    
    create_profile_window_frame = Toplevel(profilesWindow)
    create_profile_window_frame.geometry("259x95")
    create_profile_window_frame.title("New Profile")
    create_profile_window_frame.iconbitmap("./icon.ico")
    create_profile_window_frame.resizable(False, False)

    profile_name_value = StringVar()

    Label(create_profile_window_frame, text="Name:", fg="black").pack(side=TOP, anchor=NW, padx=10, pady=5)
    ttk.Entry(create_profile_window_frame, textvariable=profile_name_value).pack(padx=10, fill=X)

    buttons_frame = Frame(create_profile_window_frame)
    buttons_frame.config(pady=10)
    buttons_frame.pack()

    ttk.Button(buttons_frame, text="Ok", width=14, command=create_profile).grid(column=0, row=0, padx=5)
    ttk.Button(buttons_frame, text="Cancel", width=14, command=killWindow).grid(column=1, row=0, padx=5)

def main_window():
    global root
    global log
    global clicked
    global style
    global profileText

    root = Tk()
    root.geometry("854x510")
    root.title("Terraria Launcher")
    root.config(bg="#292929")
    root.iconbitmap("./icon.ico")
    root.resizable(False, False)

    toolbar_frame = Frame(root)
    toolbar_frame.config(bg="#292929", pady=5)
    toolbar_frame.grid(column=0, row=2, sticky=SE)

    clicked = StringVar()

    style=ttk.Style()
    style.configure("TMenubutton", width=10)
    
    Label(root, text="1.2.1 (Dev)", fg="#525252", bg="#292929").grid(column=0, row=0, sticky=NW)
    Label(root, text="This is a beta concept, some features may be unstable or not yet implemented into the launcher. You should backup your data.", fg="white", bg="#292929").grid(column=0, row=0)

    img = PhotoImage(file=background_dir)
    Label(root, image=img, highlightthickness=0, bd=0).grid(column=0, row=1)

    log = Label(root, text="Launcher has successfully loaded.", fg="red", bg="#292929", padx=5)
    log.grid(column=0, row=2, sticky=SW, pady=5)
    profileText = Label(root, text="", fg="white", bg="#292929", padx=5)
    profileText.grid(column=0, row=2, sticky=SW, pady=20)

    Label(toolbar_frame, text="Version:", fg="white", bg="#292929").grid(column=0, row=0)
    ttk.OptionMenu(toolbar_frame, clicked, versions[0], *versions, style="TMenubutton", direction="above").grid(column=1, row=0)
    ttk.Button(toolbar_frame, text="Install Version", width=14, command=version_switch).grid(column=2, row=0, padx=5)
    ttk.Button(toolbar_frame, text="Game Profiles", width=14, command=open_profiles).grid(column=1, row=1)
    ttk.Button(toolbar_frame, text="Launch Game", width=14, command=launch_game).grid(column=2, row=1, pady=5)

    update_active_profile()

    root.mainloop()

def initial_setup():
    global terrariaDir
    global versions
    global background_dir
    global savesDir

    versions = [x for x in reversed(versions)]
    background_dir = f"./backgrounds/bg{randint(0,3)}.png"

    if path.isdir("./versions/") == False:
        mkdir("./versions")
        print("Versions folder created")
    else:
        print("Versions folder located")
    if path.isdir("./profiles/") == False:
        mkdir("./profiles")
        print("Profiles folder created")
    else:
        print("Profiles folder located")
    if path.isdir("./profiles/(default profile)/") == False:
        mkdir("./profiles/(default profile)")
        print("Default profile folder created")
    else:
        print("Default profile folder located")

    try:
        f = open("config.txt", "x")
        f.write("# This is the config for the terraria version switcher.\n\n# The exact directory of your terraria install.\n# Make sure this is correct as the contents may get cleared by the version switcher.\ninstall_directory=\n# The exact directory of your terraria files, this will be used by the profile selector.\ndata_directory=")
        f.close()
    except:
        pass
    f = open("config.txt", "r")
    config_file = f.readlines()
    if config_file[4].startswith("install_directory="):
        terrariaDir = config_file[4].replace("install_directory=", "").replace("\\", "/").replace("\n", "")
    if config_file[6].startswith("data_directory="):
        savesDir = config_file[6].replace("data_directory=", "").replace("\\", "/").replace("\n", "")
    f.close()

def version_setup():
    for x in listdir("./versions/"):
        x = x.strip(".zip")
        if x not in versions:
            versions.append(x)

initial_setup()
version_setup()
main_window()
