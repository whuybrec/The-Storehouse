from tkinter import *
from tkinter.font import Font

from util import debug, info

TABS = ["/ Start", "/ Explorer"]  #, "/ Backup", "/ Torrent"]

BACKGROUND = "#000000"
FOREGROUND_A = "#FFFFFF"
FOREGROUND_P = "#7F7F7F"


class Menu:
    """
    Menu bar to navigate to other windows
    """

    def __init__(self, application):
        self.app = application
        self.tabs = []
        self.frame = LabelFrame(self.app.root, bd=0, height=50, width=1280, bg=BACKGROUND)

        self.font = Font(family="Google Sans", size=25, weight="normal")

        self.lbl_app_name = Label(
            self.frame,
            text="The Storehouse",
            bg=BACKGROUND,
            fg=FOREGROUND_A,
            font=self.font,
        )

        for tab in TABS:
            lbl = Label(
                master=self.frame,
                text=tab,
                bg=BACKGROUND,
                font=self.font,
            )
            lbl.bind("<Button-1>", self.on_menu_click)
            self.tabs.append(lbl)

        self.active_tab = self.tabs[0]

    def show(self):
        self.frame.pack(side=TOP)
        self.frame.pack_propagate(0)

        self.lbl_app_name.pack(side=RIGHT, padx=(0, 10))

        for i in range(len(self.tabs)):
            lbl = self.tabs[i]
            if i == 0:
                lbl.config(fg=FOREGROUND_A)
            else:
                lbl.config(fg=FOREGROUND_P)
            lbl.pack(side=LEFT, padx=(10, 0))

    def on_menu_click(self, event):
        debug(f"Clicked widget '{event.widget.cget('text')}'")
        if event.widget == self.active_tab:
            return

        self.active_tab.config(fg=FOREGROUND_P)
        self.active_tab = event.widget
        self.active_tab.config(fg=FOREGROUND_A)
        self.app.show(event.widget.cget("text")[2:])

