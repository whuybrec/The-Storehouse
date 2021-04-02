from .filebrowser import FileBrowser
from .sidebar import SideBar


class Explorer:
    def __init__(self, root):
        self.__file_browser__ = FileBrowser(root)
        self.__sidebar__ = SideBar(root)

    def update(self):
        self.__file_browser__.update()
        #self.__sidebar__.update()

    def show(self):
        #self.__file_browser__.show()
        self.__sidebar__.show()

    def on_hide(self):
        self.__file_browser__.on_hide()
        self.__sidebar__.on_hide()
