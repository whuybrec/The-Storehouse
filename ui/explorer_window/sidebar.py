from tkinter import *
from tkinter.font import Font
import win32api
from .drivecontainer import DriveContainer

BACKGROUND = "#181E26"
BACKGROUND_DRIVES = "#333F50"
FOREGROUND_DRIVES = "#FFFFFF"


class SideBar:
    def __init__(self, root: Widget):
        self.root = root
        self.drives = dict()

        print(win32api.GetLogicalDriveStrings())
        print(win32api.GetVolumeInformation("V:\\"))

        self.font_files = Font(family="Segoe UI Light", size=18, weight="normal")
        self.font_drives = Font(family="Google Sans", size=18, weight="normal")

        self.frame = Frame(self.root, bd=0, height=670, width=340, bg=BACKGROUND)

        self.add_drive_btn = Button(
            master=self.frame,
            bg=BACKGROUND_DRIVES,
            fg=FOREGROUND_DRIVES,
            activebackground=BACKGROUND_DRIVES,
            bd=0,
            command=self.add_drive,
            font=self.font_drives,
            text="+"
        )

        self.drives["V:\\"] = DriveContainer(self.frame, "V:\\")

    def update(self):
        pass

    def show(self):
        self.frame.place(x=0, y=50)
        self.frame.update()

        print(self.frame.winfo_height())
        self.add_drive_btn.place(
            anchor=SW,
            x=0,
            y=self.frame.winfo_height(),
            width=340,
            height=50
        )
        self.add_drive_btn.update()

        # for drive in win32api.GetLogicalDriveStrings():
        self.drives["V:\\"].show(0, 0)

    def on_hide(self):
        pass

    def add_drive(self):
        print("ADD DRIVE")
