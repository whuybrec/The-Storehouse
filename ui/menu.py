from tkinter import *
from tkinter.font import Font

TABS = ["/ Start", "/ Explorer", "/ Backup", "/ Torrent"]

BACKGROUND = "#000000"
FOREGROUND_A = "#FFFFFF"
FOREGROUND_P = "#7F7F7F"


class Menu:
    def __init__(self, application):
        self.app = application
        self.root = application.root
        self.tabs = []
        self.frame = LabelFrame(self.root, bd=0, height=50, width=1280, bg=BACKGROUND).pack(side=TOP)

        self.font = Font(family="Google Sans", size=25, weight="normal")

        self.lbl_app_name = Label(
            self.frame,
            text="The Storehouse",
            padx=10,
            bg=BACKGROUND,
            fg=FOREGROUND_A,
            font=self.font,
        )
        self.lbl_app_name.place(anchor="e", x=1280, y=25)

        x = 15
        for i in range(len(TABS)):
            if i == 0:
                lbl = Label(self.frame, text=TABS[i], bg=BACKGROUND, fg=FOREGROUND_A, font=self.font)
            else:
                lbl = Label(self.frame, text=TABS[i], bg=BACKGROUND, fg=FOREGROUND_P, font=self.font)
            lbl.bind("<Button-1>", self.on_lbl_click)
            lbl.place(anchor="w", x=x, y=25)
            lbl.update()
            self.tabs.append(lbl)
            x = lbl.winfo_x() + lbl.winfo_width() + 8

    def update(self):
        x = 15
        for i in range(len(self.tabs)):
            lbl = self.tabs[i]
            if i == 0:
                lbl.config(fg=FOREGROUND_A)
            else:
                lbl.config(fg=FOREGROUND_P)
            lbl.place(anchor="w", x=x, y=25)
            lbl.update()
            x = lbl.winfo_x() + lbl.winfo_width() + 8

    def on_lbl_click(self, event):
        if event.widget == self.tabs[0]:
            return
        self.tabs.remove(event.widget)
        self.tabs.insert(0, event.widget)
        self.update()

        self.app.display(event.widget.cget("text")[2:])
