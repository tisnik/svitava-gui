"""Main window shown on screen."""

import tkinter

from gui.menubar import *
from gui.icons import *


class MainWindow:
    """Main window shown on screen."""

    def __init__(self):
        """Initialize main window."""
        self.root = tkinter.Tk()
        self.root.title("Svitava GUI")

        self.icons = Icons()

        self.menubar = Menubar(self.root, self)
        self.root.config(menu=self.menubar)

    def show(self):
        """Display the main window on screen."""
        self.root.mainloop()

    def quit(self):
        """Display message box whether to quit the application."""
        answer = messagebox.askyesno("Do you want to quit the program?",
                                     "Do you want to quit the program?")
        if answer:
            self.root.quit()
