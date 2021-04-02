from .explorer_window import Explorer
from .start_window import Start


class WindowManager:
    def __init__(self, root):
        self.root = root

        self.__windows__ = {
            "Start": Start(self.root),
            "Explorer": Explorer(self.root)
        }

        self.__active_window__ = None

    def show(self, window):
        if self.__active_window__ is not None:
            self.__active_window__.on_hide()

        self.__active_window__ = self.__windows__[window]
        self.__active_window__.show()

    def update(self):
        self.__active_window__.update()
