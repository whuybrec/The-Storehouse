from tkinter import Frame, TOP


BACKGROUND = "#222222"


class Window:
    """
    Abstract Window class
    """
    def __init__(self, root):
        self.root = root
        self.frame = Frame(master=self.root, bd=0, height=670, width=1280, bg=BACKGROUND)

    def show(self):
        self.frame.pack(side=TOP)
        self.frame.pack_propagate(0)

    def hide(self):
        self.frame.pack_forget()

    def update(self):
        self.frame.update()
