from tkinter import *
from tkinter.font import Font
import os

BACKGROUND = "#181E26"
BACKGROUND_DRIVES = "#333F50"
FOREGROUND_DRIVES = "#FFFFFF"


class DriveContainer:
    """
    A container to hold root folders of a drive.
    """
    def __init__(self, root, path):
        self.path = path

        self.__folders_btn__ = dict()
        self.folders = [file for file in os.listdir(self.path) if not file.startswith((".", "$"))]
        self.__height__ = 0

        self.font_files = Font(family="Segoe UI Light", size=14, weight="normal")
        self.font_drives = Font(family="Google Sans", size=18, weight="normal")

        self.frame = Frame(
            master=root,
            bd=0,
            bg=BACKGROUND_DRIVES,
            width=340
        )

        for folder in self.folders:
            self.__folders_btn__[folder] = Button(
                master=self.frame,
                bg=BACKGROUND,
                fg=FOREGROUND_DRIVES,
                activebackground=BACKGROUND_DRIVES,
                activeforeground=FOREGROUND_DRIVES,
                bd=0,
                command=self.browse_files,
                font=self.font_files,
                text=folder,
                anchor=W,
                padx=25
            )

    def show(self):
        self.frame.pack(fill=X)
        self.frame.update()

        for folder in self.folders:
            self.__folders_btn__[folder].pack(fill=X)

    def hide(self):
        for folder_btn in self.__folders_btn__.values():
            folder_btn.pack_forget()

        self.frame.pack_forget()

    def get_height(self):
        return self.__height__

    def browse_files(self):
        print("BROWSE FILES")
