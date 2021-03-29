from tkinter import *
from tkinter.font import Font

TABS = ["/ Start", "/ Explorer", "/ Backup", "/ Torrent"]
BACKGROUND = "#000000"
FOREGROUND_A = "#FFFFFF"
FOREGROUND_P = "#7F7F7F"


class Application:
    def __init__(self, root):
        self.root = root
        self.tabs = []
        self.frame = LabelFrame(root, bd=0, height=50, width=1280, bg=BACKGROUND).place(x=0, y=0)

        font = Font(family="Google Sans", size=25, weight="normal")

        self.focused_lbl = Label(self.frame, text=TABS[0], bg=BACKGROUND, fg=FOREGROUND_A, font=font)
        self.focused_lbl.place(anchor="w", x=15, y=25)
        self.focused_lbl.update()

        x = self.focused_lbl.winfo_x() + self.focused_lbl.winfo_width() + 8
        for i in range(1, len(TABS)):
            lbl = Label(self.frame, text=TABS[i], bg=BACKGROUND, fg=FOREGROUND_P, font=font)
            lbl.place(anchor="w", x=x, y=25)
            lbl.update()
            self.tabs.append(lbl)
            x = lbl.winfo_x() + lbl.winfo_width() + 8

        self.lbl_app_name = Label(
            self.frame,
            text="The Storehouse",
            padx=10,
            bg=BACKGROUND,
            fg=FOREGROUND_A,
            font=font,
        )
        self.lbl_app_name.place(anchor="e", x=1280, y=25)

    def update(self):
        pass

    def on_click(self, lbl):
        # WindowManager.display(lbl.text)
        pass
