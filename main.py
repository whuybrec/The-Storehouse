from tkinter import *
from ui import Menu, WindowManager
from util import debug, info


class Application:

    def __init__(self):
        self.root = Tk()
        self.root.title("The Storehouse")
        self.root.configure(bg='#000000')
        self.root.geometry('1280x720')
        self.root.focus_force()

        self.menu = Menu(self)
        self.window_manager = WindowManager(self.root)

    def update(self):
        self.root.update()
        self.root.update_idletasks()

        self.menu.update()
        self.window_manager.update()

    def display(self, content):
        debug(f"Display: {content} window")
        self.window_manager.set(content)


if __name__ == '__main__':
    info("Starting Application.")
    window = Application()
    while True:
        window.update()
