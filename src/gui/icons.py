"""All icons used on the GUI."""

import tkinter

import icons.application_exit
import icons.help_faq
import icons.help_about


class Icons:
    """All icons used on the GUI."""

    def __init__(self):
        """Initialize all icons and convert them to PhotoImage."""
        self.exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)
        self.help_faq_icon = tkinter.PhotoImage(data=icons.help_faq.icon)
        self.help_about_icon = tkinter.PhotoImage(data=icons.help_about.icon)
