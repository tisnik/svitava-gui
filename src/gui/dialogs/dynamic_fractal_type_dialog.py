import tkinter


class DynamicFractalTypeDialog(tkinter.Toplevel):

    def __init__(self, parent):
        """
        Initialize the DynamicFractalTypeDialog as a Toplevel window attached to the given parent.

        Parameters:
            parent: The parent Tk or widget to which this dialog window will be attached.
        """
        tkinter.Toplevel.__init__(self, parent)
        top_part = tkinter.LabelFrame(self, text="Dynamic fractal", padx=5, pady=5)
        top_part.grid(row=1, column=1, sticky="NWSE")

        # rest
        cancelButton = tkinter.Button(self, text="Cancel", command=self.cancel)
        cancelButton.grid(row=2, column=1, sticky="NWSE")

        # how the buttons should behave
        self.bind("<Escape>", lambda event: self.destroy())

        # don't display the dialog in list of opened windows
        self.transient(parent)

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()
        self.parent = parent
        cancelButton.focus_set()

    def cancel(self):
        """
        Close the dialog window.

        Destroys the Toplevel window, closing the dialog and releasing its associated resources.
        """
        self.destroy()

    def show(self):
        """
        Display the dialog (restore if minimized) and block until the window is closed.

        This brings the dialog to the foreground if it was minimized and then waits for the dialog window to be destroyed, preventing code execution from continuing until the user closes the dialog.
        """
        self.wm_deiconify()
        self.wait_window()
