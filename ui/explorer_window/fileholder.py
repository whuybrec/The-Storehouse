from tkinter import *
from tkinter.font import Font

from util import debug

FOREGROUND = "#FFFFFF"


class FileHolder:
    """
    A holder for a file or folder.
    """

    def __init__(self, root, path, background):
        self.root = root
        self.path = path

        self.font = Font(family="Segoe UI Light", size=16, weight="normal")
        self.frame = Frame(self.root, bd=0, bg=background, height=35)
        self.frame.bind("<Button-1>", self.on_item_click)
        self.file_lbl = Label(
            master=self.frame,
            text=path.split("/")[-1],
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.file_lbl.bind("<Button-1>", self.on_item_click)
        self.modified_lbl = Label(
            master=self.frame,
            text="MODIFIED",
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.modified_lbl.bind("<Button-1>", self.on_item_click)
        self.size_lbl = Label(
            master=self.frame,
            text="SIZE",
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
        self.modified_lbl.place(relx=0.8, rely=0.5, anchor=CENTER)
        self.size_lbl.pack(side=RIGHT, padx=(0, 10))

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
