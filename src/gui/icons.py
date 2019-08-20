"""All icons used on the GUI."""

import tkinter

import icons.application_exit

class Icons:
    """All icons used on the GUI."""

    def __init__(self):
        """Initialize all icons and convert them to PhotoImage."""
        self.exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)
