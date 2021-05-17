from util import debug
from tkinter import *
from .filebrowser import FileBrowser
from .sidebar import SideBar
from ..window import Window


class Explorer(Window):
    """
    Explorer window to navigate through drives, files and folders.
    """
    def __init__(self, root):
        super().__init__(root)
        self.__sidebar__ = SideBar(self.frame, self)
        self.__file_browser__ = FileBrowser(self.frame)

    def update(self):
        super().update()
        self.__sidebar__.update()
        self.__file_browser__.update()

    def show(self):
        super().show()
        self.__sidebar__.show()
        self.__file_browser__.show()

    def hide(self):
        super().hide()
        # self.__file_browser__.on_hide()

    def browse(self, path):
        debug(f"Browse folder: {path}")
        self.__file_browser__.browse(path)
