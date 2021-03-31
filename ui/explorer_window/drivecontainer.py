from tkinter import *
from tkinter.font import Font
import win32api

BACKGROUND = "#181E26"
BACKGROUND_DRIVES = "#333F50"
FOREGROUND_DRIVES = "#FFFFFF"


class DriveContainer:
    def __init__(self, root, path):
        self.root = root
        self.path = path
        try:
            self.name = win32api.GetVolumeInformation(self.path)[0]
        except IndexError:
            self.name = self.path

        self.__height__ = 0

        self.font_files = Font(family="Segoe UI Light", size=18, weight="normal")
        self.font_drives = Font(family="Google Sans", size=18, weight="normal")

        self.__drive_btn__ = Button(
            master=self.root,
            bg=BACKGROUND_DRIVES,
            fg=FOREGROUND_DRIVES,
            activebackground=BACKGROUND_DRIVES,
            bd=0,
            command=self.toggle,
            font=self.font_drives,
            text=self.name
        )

    def show(self, x, y):
        self.__drive_btn__.place(x=x, y=y, width=340, height=50)
        self.__drive_btn__.update()

    def get_height(self):
        return self.__height__

    def toggle(self):
        print("TOGGLE")
