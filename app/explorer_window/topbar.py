from tkinter import *
from tkinter.font import Font


BACKGROUND_1 = "#222222"
BACKGROUND_2 = "#303030"
FOREGROUND = "#FFFFFF"


class TopBar:
    """
    Represents the topBar that contains current path and back/forward buttons
    """

    def __init__(self, filebrowser, root):
        self.fileBrowser = filebrowser
        self.root = root

        self.font = Font(family="Google Sans", size=18, weight="normal")
        self.frame = Frame(self.root, bd=0, bg=BACKGROUND_1)

        self.path = []
        self.path_lbls = []

    def update(self):
        self.frame.update()

    def show(self):
        self.frame.pack(side=TOP, fill=X)
        for lbl in self.path_lbls:
            lbl.pack(side=LEFT, padx=(5, 0))

    def on_path_click(self, event):
        length = self.path_lbls.index(event.widget) + 1
        path = "/".join(self.path[:length])
        self.fileBrowser.browse(path)

    def set(self, path):
        for lbl in self.path_lbls:
            lbl.destroy()

        self.path = []
        self.path_lbls = []
        for folder in path.split("/"):
            if folder == "":
                continue
            lbl = Label(
                master=self.frame,
                text=folder + "/",
                bg=BACKGROUND_1,
                fg=FOREGROUND,
                font=self.font,
                padx=5
            )
            lbl.bind("<Button-1>", self.on_path_click)
            self.path_lbls.append(lbl)
            self.path.append(folder)
        self.show()
