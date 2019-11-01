"""Main window shown on screen."""

import tkinter

from gui.canvas import *
from gui.menubar import *
from gui.icons import *


class MainWindow:
    """Main window shown on screen."""

    def __init__(self):
        """Initialize main window."""
        self.root = tkinter.Tk()
        self.root.title("Svitava GUI")

        self.icons = Icons()

        self.canvas = Canvas(self.root, 800, 600, self)

        self.configure_grid()
        self.canvas.grid(column=1, row=1, sticky="NWSE")

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

    def configure_grid(self):
        """Configure grid on canvas."""
        tkinter.Grid.rowconfigure(self.root, 2, weight=1)
        tkinter.Grid.columnconfigure(self.root, 2, weight=1)
