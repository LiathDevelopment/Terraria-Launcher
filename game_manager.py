from launcher_handler import *

from webbrowser import open as openURL

def launch_game(root):
    try:
        print("" - 1)
        openURL("steam://rungameid/105600")
    except:
        error_window(root, "Terraria launch failed", "Has Steam been installed?")
