from tkinter import *
from tkinter.font import Font
import win32api
from .drivecontainer import DriveContainer

BACKGROUND = "#181E26"
BACKGROUND_DRIVES = "#333F50"
FOREGROUND_DRIVES = "#FFFFFF"


class SideBar:
    """
    Represents the sidebar that contains drives and root folders.
    """
    def __init__(self, root: Widget):
        self.root = root
        self.drives = dict()

        self.font_files = Font(family="Segoe UI Light", size=18, weight="normal")
        self.font_drives = Font(family="Google Sans", size=18, weight="normal")

        self.frame = Frame(self.root, bd=0, bg=BACKGROUND, height=670, width=340)

        self.add_drive_btn = Button(
            master=self.frame,
            bg=BACKGROUND_DRIVES,
            fg=FOREGROUND_DRIVES,
            activebackground=BACKGROUND_DRIVES,
            activeforeground=FOREGROUND_DRIVES,
            bd=0,
            command=self.add_drive,
            font=self.font_drives,
            text="+"
        )

        for path in win32api.GetLogicalDriveStrings().split("\x00"):
            if path == '':
                continue

            try:
                name = win32api.GetVolumeInformation(path)[0]
            except Exception as e:
                print(e)
                name = path

            btn = Button(
                master=self.frame,
                bg=BACKGROUND_DRIVES,
                fg=FOREGROUND_DRIVES,
                activebackground=BACKGROUND_DRIVES,
                activeforeground=FOREGROUND_DRIVES,
                bd=0,
                font=self.font_drives,
                text=name,
            )
            btn.bind("<Button-1>", self.on_drive_click)
            self.drives[name] = {"Drive": btn, "Container": DriveContainer(self.frame, path), "Show": True}

    def update(self):
        pass

    def show(self):
        self.frame.pack(side=LEFT, fill=BOTH)
        self.frame.pack_propagate(0)
        self.frame.update()

        self.add_drive_btn.pack(side=BOTTOM, fill=X)
        self.add_drive_btn.update()

        for (path, dct) in self.drives.items():
            (drive_btn, container, show) = (dct["Drive"], dct["Container"], dct["Show"])
            drive_btn.pack_forget()
            drive_btn.pack(fill=X)
            if show:
                container.show()

    def on_hide(self):
        self.frame.pack_forget()
        self.hide_drives()

    def add_drive(self):
        print("ADD DRIVE")

    def on_drive_click(self, event):
        name = event.widget.cget("text")
        obj = self.drives[name]
        if obj["Show"]:
            obj["Show"] = False
        else:
            obj["Show"] = True

        self.hide_drives()
        self.show()

    def hide_drives(self):
        for (path, dct) in self.drives.items():
            (drive_btn, container, show) = (dct["Drive"], dct["Container"], dct["Show"])
            drive_btn.pack_forget()
            container.hide()
