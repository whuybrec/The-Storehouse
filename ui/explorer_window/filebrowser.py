from tkinter import *
from .topbar import TopBar
from .fileholder import FileHolder
import os

BACKGROUND_1 = "#222222"
BACKGROUND_2 = "#303030"
FOREGROUND = "#FFFFFF"


class FileBrowser:
    def __init__(self, root):
        self.frame = Frame(master=root, bd=0, bg=BACKGROUND_1)
        self.topbar = TopBar(self.frame)
        self.folders = []

    def update(self):
        self.frame.update()
        self.topbar.update()

    def show(self):
        self.frame.place(x=340, y=0, width=940, height=670)
        self.topbar.show()
        for folder in self.folders:
            folder.show()

    def hide(self):
        self.frame.pack_forget()
        self.topbar.hide()
        for folder in self.folders:
            folder.hide()

    def browse(self, path):
        self.topbar.set(path)
        self.hide()

        self.folders = []
        folders = os.listdir(path)
        for i in range(len(folders)):
            if i % 2 == 0:
                self.folders.append(FileHolder(self.frame, (path + "/" + folders[i]), BACKGROUND_2))
            else:
                self.folders.append(FileHolder(self.frame, (path + "/" + folders[i]), BACKGROUND_1))
        self.show()
