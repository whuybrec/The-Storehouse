from datetime import datetime
from tkinter import *
from tkinter.font import Font
from util import debug
from PIL import Image, ImageTk
import os
from win32comext.shell import shell
import win32api
import win32con
import win32ui
import win32gui


FOREGROUND = "#FFFFFF"
CWD = os.getcwd()
SIZES = [" B", " KB", " MB", " GB", " TB"]
SHGFI_ICON = 0x000000100
SHGFI_ICONLOCATION = 0x000001000
SHIL_SIZE = 0x00001


class FileHolder:
    """
    A holder for a file or folder.
    """

    def __init__(self, filebrowser, root, path, background):
        self.filebrowser = filebrowser
        self.root = root
        self.path = "/".join([f for f in path.split("/") if f != ""])

        self.file = path.split("/")[-1]
        self.size = os.stat(path).st_size / 800
        cnt = 0
        while self.size > 100:
            cnt += 1
            self.size = self.size / 100
        self.size = str(round(self.size, 2)) + SIZES[cnt]
        self.modified = datetime.utcfromtimestamp(os.stat(path).st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        self.font = Font(family="Segoe UI", size=16, weight="normal")
        self.frame = Frame(self.root, bd=0, bg=background, height=35)
        self.frame.bind('<Double-Button-1>', self.on_item_click)
        if self.font.measure(self.file) > 500:
            while self.font.measure(self.file) > 500:
                self.file = self.file[:-1]
            self.file += "..."

        self.file_lbl = Label(
            master=self.frame,
            text=self.file,
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.file_lbl.bind('<Double-Button-1>', self.on_item_click)
        self.modified_lbl = Label(
            master=self.frame,
            text=self.modified,
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.modified_lbl.bind('<Double-Button-1>', self.on_item_click)
        self.size_lbl = Label(
            master=self.frame,
            text=self.size,
            bg=background,
            fg=FOREGROUND,
            font=self.font,
        )
        self.size_lbl.bind('<Double-Button-1>', self.on_item_click)

        if os.path.isdir(self.path):
            ext = "__FOLDER__"
        else:
            ext = self.path.split(".")[-1]

        print(len(self.filebrowser.icons.keys()))
        if ext in self.filebrowser.icons.keys():
            image = self.filebrowser.icons[ext]
        else:
            image = self.get_icon(self.path)
            image = image.resize((25, 25), Image.ANTIALIAS)
            self.filebrowser.icons[ext] = image

        tk_image = ImageTk.PhotoImage(image)
        self.image_lbl = Label(
            master=self.frame,
            bg=background,
            image=tk_image
        )
        self.image_lbl.image = tk_image

    def update(self):
        self.frame.update()
        self.file_lbl.update()
        self.modified_lbl.update()
        self.size_lbl.update()
        self.image_lbl.update()

    def show(self):
        self.frame.pack(side=TOP, fill=X)
        self.frame.pack_propagate(0)
        self.image_lbl.pack(side=LEFT, padx=(10, 5))
        self.file_lbl.pack(side=LEFT)
        self.size_lbl.pack(side=RIGHT, padx=(0, 10))
        self.modified_lbl.place(relx=0.6, rely=0)

    def hide(self):
        self.frame.destroy()
        self.file_lbl.destroy()
        self.modified_lbl.destroy()
        self.size_lbl.destroy()
        self.image_lbl.destroy()

    def on_item_click(self, event=None):
        debug(f"Clicked file '{self.path}'")
        self.filebrowser.open_(self.path)

    def bind(self, button, call):
        self.frame.bind(button, call)
        self.file_lbl.bind(button, call)
        self.modified_lbl.bind(button, call)
        self.size_lbl.bind(button, call)
        self.image_lbl.bind(button, call)

    @staticmethod
    def get_icon(path):
        path = path.replace("/", "\\")
        ret, info = shell.SHGetFileInfo(path, 0, SHGFI_ICONLOCATION | SHGFI_ICON | SHIL_SIZE)
        icon, _, _, _, _ = info
        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), icon)
        win32gui.DestroyIcon(icon)
        bmpinfo = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)
        img = Image.frombuffer("RGBA", (bmpinfo["bmWidth"], bmpinfo["bmHeight"]), bmpstr, "raw", "BGRA", 0, 1)
        return img
