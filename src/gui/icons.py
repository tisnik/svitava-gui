"""All icons used on the GUI."""

import tkinter

import icons.application_exit
import icons.help_faq
import icons.help_about
import icons.fractal_new
import icons.file_open
import icons.file_save
import icons.file_save_as
import icons.edit


class Icons:
    """All icons used on the GUI."""

    def __init__(self):
        """Initialize all icons and convert them to PhotoImage."""
        self.exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)
        self.help_faq_icon = tkinter.PhotoImage(data=icons.help_faq.icon)
        self.help_about_icon = tkinter.PhotoImage(data=icons.help_about.icon)
        self.fractal_new_icon = tkinter.PhotoImage(data=icons.fractal_new.icon)

        self.file_open_icon = tkinter.PhotoImage(data=icons.file_open.icon)
        self.file_save_icon = tkinter.PhotoImage(data=icons.file_save.icon)
        self.file_save_as_icon = tkinter.PhotoImage(data=icons.file_save_as.icon)

        self.edit_icon = tkinter.PhotoImage(data=icons.edit.icon)
