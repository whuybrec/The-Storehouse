from tkinter import *
from ui import Menu, WindowManager
from util import debug, info


class Application:

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

    def update(self):
        self.root.update()
        self.root.update_idletasks()

        self.window_manager.update()

    def display(self, content):
        debug(f"Display: {content} window")
        self.window_manager.show(content)


if __name__ == '__main__':
    info("Starting Application.")
    window = Application()
    while True:
        window.update()
