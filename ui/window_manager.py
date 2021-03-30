

class WindowManager:
    def __init__(self, root):
        self.active_window = None
        self.windows = {
            "Start": self.set_start_window,
            "Explorer": self.set_explorer_window,
            "Backup": self.set_backup_winodw,
            "Torrent": self.set_torrent_window
        }

    def set(self, window):
        pass

    def set_explorer_window(self):
        pass

    def set_start_window(self):
        pass

    def set_torrent_window(self):
        pass

    def set_backup_winodw(self):
        pass

    def update(self):
        pass
        #self.active_window.update()
