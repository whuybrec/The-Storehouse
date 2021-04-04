from datetime import datetime
from tkinter import *
from tkinter.font import Font
import os
from util import debug

FOREGROUND = "#FFFFFF"


class FileHolder:
    """
    A holder for a file or folder.
    """

    def __init__(self, root, path, background):
        self.root = root
        self.path = path
        self.file = path.split("/")[-1]
        self.size = str(round((os.stat(path).st_size / 800), 2)) + " KB"
        self.modified = datetime.utcfromtimestamp(os.stat(path).st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        self.font = Font(family="Segoe UI", size=16, weight="normal")
        self.frame = Frame(self.root, bd=0, bg=background, height=35)
        self.frame.bind("<Button-1>", self.on_item_click)
        if self.font.measure(self.file) > 500:
            while self.font.measure(self.file) > 500:
                self.file = self.file[:-1]
            self.file += "..."

        self.file_lbl = Label(
            master=self.frame,
            text=self.file,
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.file_lbl.bind("<Button-1>", self.on_item_click)
        self.modified_lbl = Label(
            master=self.frame,
            text=self.modified,
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.modified_lbl.bind("<Button-1>", self.on_item_click)
        self.size_lbl = Label(
            master=self.frame,
            text=self.size,
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.size_lbl.bind("<Button-1>", self.on_item_click)

    def update(self):
        self.frame.update()
        self.file_lbl.update()
        self.modified_lbl.update()
        self.size_lbl.update()

    def show(self):
        self.frame.pack(side=TOP, fill=X)
        self.frame.pack_propagate(0)
        self.file_lbl.pack(side=LEFT, padx=(10, 0))
        self.file_lbl.pack_propagate(0)
        self.size_lbl.pack(side=RIGHT, padx=(0, 10))
        self.modified_lbl.place(relx=0.6, rely=0)

    def hide(self):
        self.frame.destroy()
        self.file_lbl.destroy()
        self.modified_lbl.destroy()
        self.size_lbl.destroy()

    def on_item_click(self, event):
        debug(f"Clicked item '{event.widget}'")

    def bind(self, button, call):
        self.frame.bind(button, call)
        self.file_lbl.bind(button, call)
        self.modified_lbl.bind(button, call)
        self.size_lbl.bind(button, call)
