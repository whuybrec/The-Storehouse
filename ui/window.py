from tkinter import Frame, TOP


class Window:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(master=self.root, bd=0, height=670, width=1280, bg="#222222")

    def show(self):
        self.frame.pack(side=TOP)
        self.frame.pack_propagate(0)

    def on_hide(self):
        self.frame.pack_forget()

    def update(self):
        pass
