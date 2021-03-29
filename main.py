from tkinter import *
from ui import Application


class Window:

    def __init__(self):
        self.root = Tk()
        self.root.title("The Storehouse")
        self.root.configure(bg='#000000')
        self.root.geometry('1280x720')
        self.root.focus_force()

        self.menu = Application(self.root)

    def update(self):
        self.root.update()
        self.root.update_idletasks()

        # self.menu.update()
        # self.canvas.update()


if __name__ == '__main__':
    window = Window()
    while True:
        window.update()
