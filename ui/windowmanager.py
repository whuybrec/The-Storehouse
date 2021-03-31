from explorer_window import Explorer


class WindowManager:
    def __init__(self, root):
        self.root = root
        self.active_window = None

        self.windows = {
            #"Start": self.show_start_window,
            "Explorer": Explorer(),
            #"Backup": self.show_backup_winodw,
            #"Torrent": self.show_torrent_window
        }

    def show(self, window):
        pass

    def update(self):
        pass
        #self.active_window.update()
