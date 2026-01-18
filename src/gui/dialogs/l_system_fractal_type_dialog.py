"""Dialog to select L-system."""

#
#  (C) Copyright 2026  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import tkinter


class LSystemFractalTypeDialog(tkinter.Toplevel):

    def __init__(self, parent):
        """
        Initialize the LSystemFractalTypeDialog attached to the given parent window.

        Parameters:
            parent (tkinter.Widget): The parent or master window that will own this dialog.
        """
        tkinter.Toplevel.__init__(self, parent)
        top_part = tkinter.LabelFrame(self, text="L-systems", padx=5, pady=5)
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

        This brings the dialog to the foreground if it was minimized and then
        waits for the dialog window to be destroyed, preventing code execution
        from continuing until the user closes the dialog.
        """
        self.wm_deiconify()
        self.wait_window()
