from .explorer_window import Explorer


class WindowManager:
    def __init__(self, root):
        self.root = root

        self.__windows__ = {
            "Explorer": Explorer(self.root)
        }

        self.__active_window__ = self.__windows__["Explorer"]
        self.__active_window__.show()

    def show(self, window):
        pass
        # self.__active_window__.on_hide()
        # self.__windows__[window].show()

    def update(self):
        self.__active_window__.update()
