from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
import win32api
import os
import json
from .driveholder import DriveHolder

BACKGROUND = "#181E26"
BACKGROUND_DRIVES = "#333F50"
FOREGROUND_DRIVES = "#FFFFFF"

FILE = "explorer.json"
DIRECTORY = "bin"

# TODO:
#   - add option to scroll


class SideBar:
    """
    Represents the sidebar that contains drives and root folders.
    """
    def __init__(self, root: Widget, explorer):
        self.root = root
        self.explorer = explorer
        self.drives = []
        self.names_dict = dict()

        self.font_drives = Font(family="Google Sans", size=14, weight="normal")
        self.frame = Frame(self.root, bd=0, bg=BACKGROUND)
        self.add_drive_btn = Button(
            master=self.frame,
            bg=BACKGROUND_DRIVES,
            fg=FOREGROUND_DRIVES,
            activebackground=BACKGROUND_DRIVES,
            activeforeground=FOREGROUND_DRIVES,
            bd=0,
            command=self.select_drive,
            font=self.font_drives,
            text="+"
        )

        data = self.read_()
        for path in data["drives"]:
            self.add_drive(path)

    def update(self):
        self.frame.update()
        for drive in self.drives:
            drive.update()
        self.add_drive_btn.update()

    def show(self):
        self.frame.place(x=0, y=0, width=340, height=670)
        for drive in self.drives:
            drive.show()
        self.add_drive_btn.pack(side=TOP, fill=X)

    def hide(self):
        self.frame.pack_forget()
        for drive in self.drives:
            drive.hide()
        self.add_drive_btn.pack_forget()

    def select_drive(self):
        path = filedialog.askdirectory(initialdir="/", title="Select a Directory")
        self.add_drive(path)

        self.hide()
        self.show()

        self.write_()

    def add_drive(self, path):
        if path.endswith("/"):
            name = win32api.GetVolumeInformation(path)[0]
        else:
            name = path.split("/")[-1]
        folders = [f for f in os.listdir(path) if not f.startswith((".", "$"))]
        self.names_dict[name] = path
        self.drives.append(DriveHolder(self.frame, self, name, folders))

    def browse_folder(self, drive_name, folder):
        path = self.names_dict[drive_name] + "/" + folder
        self.explorer.browse(path)

    # def scroll(self, event):
    #     self.height = self.frame.winfo_height()
    #     scroll_y = self.scroll_y + event.delta
    #     if 0 > scroll_y > 670-self.height:
    #         self.scroll_y = scroll_y
    #         self.frame.place(x=0, y=self.scroll_y)

    @staticmethod
    def read_():
        parent_dir = os.path.join(os.getcwd(), DIRECTORY)
        if not os.path.exists(parent_dir):
            os.mkdir(parent_dir)
        path = os.path.join(parent_dir, FILE)
        try:
            with open(path) as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return {"drives": []}

    def write_(self):
        data = dict()
        data["drives"] = []
        for path in self.names_dict.values():
            data["drives"].append(path)

        path = os.path.join(os.getcwd(), DIRECTORY, FILE)
        with open(path, "w") as f:
            json.dump(data, f)
