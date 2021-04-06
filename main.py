import time
from tkinter import *
from ui import Menu, WindowManager
from util import debug, info


class Application:
    """
    NAS GUI Application aka "The Storehouse"
    """

    def __init__(self):
        self.root = Tk()
        self.root.title("The Storehouse")
        self.root.configure(bg='#000000')
        self.root.geometry('1280x720')
        self.root.resizable(False, False)
        self.root.focus_force()
        self.root.update()

        self.menu = Menu(self)
        self.menu.show()

        self.window_manager = WindowManager(self.root)
        self.window_manager.show("Start")

        self.fps_counter = Label(master=self.root, bg='#000000', fg='#FFFFFF')
        self.fps_counter.place(anchor=SE, x=1280, y=720)

        self.time_ = time.time()
        self.frames = 0

    def update(self):
        self.root.update()
        self.root.update_idletasks()

        self.window_manager.update()

        self.frames += 1
        time_b = time.time()
        diff = time_b - self.time_
        if diff > 1:
            self.fps_counter.config(text=str(self.frames) + " fps")
            self.frames = 0
            self.time_ = time.time()

    def show(self, content):
        self.window_manager.show(content)


if __name__ == '__main__':
    info("Starting Application.")
    window = Application()
    while True:
        window.update()
