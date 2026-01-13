"""Implementation of application settings dialog."""

import tkinter


class SettingsDialog(tkinter.Toplevel):
    """Implementation of application settings dialog."""

    def __init__(self, parent) -> None:
        """Initialize the dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Settings")

        # don't display the dialog in list of opened windows
        self.transient(parent)

        self.group1 = tkinter.LabelFrame(self, text="Renderer", padx=5, pady=8)
        self.group2 = tkinter.LabelFrame(self, text="User interface", padx=5, pady=8)
        self.group3 = tkinter.LabelFrame(self, text="Directories", padx=5, pady=8)

        # frame group #1
        l = tkinter.Label(self.group1, text="Test")
        l.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        self.group1.grid(row=1, column=1, sticky="WE")

        # frame group #2
        l = tkinter.Label(self.group2, text="Test")
        l.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        self.group2.grid(row=2, column=1, sticky="WE")

        # frame group #3
        self.group3.grid(row=3, column=1, sticky="WE")
        l = tkinter.Label(self.group3, text="Test")
        l.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        # rest
        okButton = tkinter.Button(self, text="OK", command=self.ok)
        okButton.grid(row=4, column=1, sticky="W")

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # how the buttons should behave
        self.bind("<Return>", lambda event: self.ok())
        self.bind("<Escape>", lambda event: self.destroy())

        # get the focus
        okButton.focus_set()

    def ok(self) -> None:
        """Handle Ok button press."""
        self.destroy()


def settings_dialog(parent):
    """
    Open the "Settings" dialog.
    """
    SettingsDialog(parent)
