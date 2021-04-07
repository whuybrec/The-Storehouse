from tkinter import *
from .topbar import TopBar
from .fileholder import FileHolder
import os

BACKGROUND_1 = "#222222"
BACKGROUND_2 = "#303030"
FOREGROUND = "#FFFFFF"


class FileBrowser:
    """
    A file browser class to navigate through folders and open files.
    """

    def __init__(self, root):
        self.frame = Frame(master=root, bd=0, bg=BACKGROUND_1, width=940, height=670)
        self.topbar = TopBar(self, self.frame)

        self.frame_folders = Frame(master=self.frame, bd=0, bg=BACKGROUND_1)
        self.scrollable_frame = Frame(master=self.frame_folders, bd=0, bg=BACKGROUND_1)
        self.folders = []
        self.height = 670
        self.scroll_y = 0
        self.icons = dict()

    def update(self):
        self.frame.update()
        self.frame_folders.update()
        self.scrollable_frame.update()
        self.topbar.update()

    def show(self):
        self.frame.pack(side=RIGHT)
        self.frame.pack_propagate(0)
        self.frame_folders.place(x=0, y=35, width=940, height=670)
        self.scrollable_frame.place(x=0, y=0, width=940, height=self.height)
        self.topbar.show()
        for folder in self.folders:
            folder.show()

    def hide(self):
        self.frame.pack_forget()
        self.frame_folders.place_forget()
        self.scrollable_frame.place_forget()
        self.topbar.hide()
        for folder in self.folders:
            folder.hide()
        self.height = 0
        self.scroll_y = 0

    def browse(self, path):
        self.topbar.set(path)
        self.hide()

        self.height = 0
        self.scroll_y = 0
        self.folders = []
        folders = os.listdir(path)
        for i in range(len(folders)):
            if i % 2 == 0:
                fh = FileHolder(self, self.scrollable_frame, (path + "/" + folders[i]), BACKGROUND_2)
            else:
                fh = FileHolder(self, self.scrollable_frame, (path + "/" + folders[i]), BACKGROUND_1)
            self.folders.append(fh)
            fh.bind("<MouseWheel>", self.scroll)
            self.height += 35
        self.show()

    def open_(self, path):
        if os.path.isfile(path):
            os.startfile(path)
        else:
            self.browse(path)

    def scroll(self, event):
        if self.height < 670:
            return
        scroll_y = self.scroll_y + event.delta
        if 0 < scroll_y:
            self.scroll_y = 0
        elif scroll_y < 670-self.height:
            self.scroll_y = 670-self.height
        else:
            self.scroll_y = scroll_y
        self.scrollable_frame.place(x=0, y=self.scroll_y, width=940, height=self.height)
