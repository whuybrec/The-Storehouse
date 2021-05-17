from util import debug
from .explorer_window import Explorer
from .start_window import Start


class WindowManager:
    """
    Manages transitions to other windows
    """
    def __init__(self, root):
        self.root = root

        self.__windows__ = {
            "Start": Start(self.root),
            "Explorer": Explorer(self.root)
        }

        self.active_window = None

    def show(self, window):
        debug(f"Show '{window}' window")
        if self.active_window is not None:
            self.active_window.hide()

        self.active_window = self.__windows__[window]
        self.active_window.show()

    def update(self):
        self.active_window.update()
