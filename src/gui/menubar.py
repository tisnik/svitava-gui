"""Menu bar displayed on the main window."""

import tkinter

from gui.dialogs.about_dialog import *


class Menubar(tkinter.Menu):
    """Menu bar displayed on the main window."""

    def __init__(self, parent, main_window):
        """Initialize the menu bar."""
        super().__init__(tearoff=0)

        self.parent = parent
        self.main_window = main_window

        self.filemenu = tkinter.Menu(self, tearoff=0)
        self.filemenu.add_command(label="Quit", image=main_window.icons.exit_icon,
                                  compound="left", underline=0, accelerator="Ctrl+Q",
                                  command=parent.quit)


        self.renderermenu = tkinter.Menu(self, tearoff=0)
        self.renderermenu.add_command(label="New fractal", image=main_window.icons.fractal_new_icon,
                                     compound="left", underline=0, accelerator="Ctrl+N")

        self.compositormenu = tkinter.Menu(self, tearoff=0)

        self.helpmenu = tkinter.Menu(self, tearoff=0)
        self.helpmenu.add_command(label="Help",
                                  image=main_window.icons.help_faq_icon,
                                  compound="left", underline=0, accelerator="F1",
                                  command=help)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About",
                                  image=main_window.icons.help_about_icon, accelerator="F11",
                                  compound="left", underline=0, command=about)

        self.add_cascade(label="File", menu=self.filemenu, underline=0)
        self.add_cascade(label="Renderer", menu=self.renderermenu, underline=0)
        self.add_cascade(label="Compositor", menu=self.compositormenu, underline=0)
        self.add_cascade(label="Help", menu=self.helpmenu, underline=0)

        self.parent.bind('<F1>', lambda event: help())
        self.parent.bind('<F11>', lambda event: about())
