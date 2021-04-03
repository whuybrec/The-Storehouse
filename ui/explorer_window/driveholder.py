from tkinter import *
from tkinter.font import Font
from util import debug

BACKGROUND = "#181E26"
BACKGROUND_DRIVES = "#333F50"
FOREGROUND_DRIVES = "#FFFFFF"


class DriveHolder:
    """
    A container to hold a drive with the drive's root folders.
    """
    def __init__(self, root, sidebar, name, folders):
        self.sidebar = sidebar
        self.name = name
        self.folders = []
        self.visable = True

        self.font_drives = Font(family="Google Sans", size=14, weight="normal")
        self.font_files = Font(family="Segoe UI Light", size=12, weight="normal")

        self.container = Frame(master=root, bg=BACKGROUND)
        self.drive_btn = Button(
            master=self.container,
            bg=BACKGROUND_DRIVES,
            fg=FOREGROUND_DRIVES,
            activebackground=BACKGROUND_DRIVES,
            activeforeground=FOREGROUND_DRIVES,
            bd=0,
            command=self.toggle_folders_visability,
            font=self.font_drives,
            text=name,
        )

        self.frame_folders = Frame(master=self.container, bg=BACKGROUND)
        for folder in folders:
            btn = Button(
                master=self.frame_folders,
                bg=BACKGROUND,
                fg=FOREGROUND_DRIVES,
                activebackground=BACKGROUND,
                activeforeground=FOREGROUND_DRIVES,
                bd=0,
                font=self.font_files,
                text=folder,
                anchor=W,
                padx=25
            )
            btn.bind("<Button-1>", self.browse_folder)
            self.folders.append(btn)

    def show(self):
        self.container.pack(side=TOP, fill=X)
        self.drive_btn.pack(side=TOP, fill=X)
        for folder in self.folders:
            folder.pack(side=TOP, fill=X)

        if not self.visable:
            return
        self.frame_folders.pack(side=TOP, fill=X)

    def update(self):
        self.container.update()
        self.drive_btn.update()
        self.frame_folders.update()
        for folder in self.folders:
            folder.update()

    def hide(self):
        self.container.pack_forget()
        self.drive_btn.pack_forget()
        self.frame_folders.pack_forget()
        for folder in self.folders:
            folder.pack_forget()

    def toggle_folders_visability(self):
        if self.visable:
            self.frame_folders.pack_forget()
            self.visable = False
        else:
            self.frame_folders.pack(side=TOP, fill=X)
            self.visable = True

        debug(f"Visibility for folders of drive '{self.name}' is set to '{self.visable}'")

    def browse_folder(self, event):
        debug(f"Browse to folder '{event.widget.cget('text')}' of drive '{self.name}'")
        self.sidebar.browse_folder(self.name, event.widget.cget('text'))
