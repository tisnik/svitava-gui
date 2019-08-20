"""Menu bar displayed on the main window."""

import tkinter

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


        self.add_cascade(label="File", menu=self.filemenu, underline=0)
