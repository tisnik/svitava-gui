"""Implementation of 'Select pattern type' dialog."""

#
#  (C) Copyright 2019, 2020  Pavel Tisnovsky
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
from renderer import cached_image


class PatternTypeDialog(tkinter.Toplevel):

    def __init__(self, parent: tkinter.Tk) -> None:
        """
        Initialize the pattern type selection dialog as a modal top-level window.

        Parameters:
            parent: The parent widget for this dialog (typically a tkinter root or window).
        """
        tkinter.Toplevel.__init__(self, parent)
        top_part = tkinter.LabelFrame(self, text="Fractal type", padx=5, pady=5)
        top_part.grid(row=1, column=1, sticky="NWSE")

        self.image = tkinter.PhotoImage(data=cached_image("image1.ppm"))
        button = tkinter.Button(top_part)
        button.config(text="Foo", image=self.image, compound=tkinter.TOP)
        button.grid(row=1, column=1)

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
        # _cplx_button.focus_set()

    def cancel(self):
        """
        Close and destroy the dialog window.
        """
        self.destroy()

    def show(self):
        """
        Show the dialog and block execution until the window is closed.

        This deiconifies the toplevel window and waits for it to be destroyed, returning control after the dialog is closed.
        """
        self.wm_deiconify()
        self.wait_window()
        # return self.rooms, self.id.get()

    def on_cplx_clicked(self):
        """
        Open the dialog for selecting or configuring a complex-plane fractal type.
        """
        ComplexFractalTypeDialog(self)

    def on_dynamic_clicked(self):
        """
        Open the "Dynamic system" fractal type dialog.

        Instantiates a DynamicFractalTypeDialog with no parent.
        """
        DynamicFractalTypeDialog(self)

    def on_ifs_clicked(self):
        """
        Open the IFS fractal type selection dialog.

        Creates an IFSFractalTypeDialog with no parent window, triggering the dialog UI for configuring an IFS fractal.
        """
        IFSFractalTypeDialog(self)

    def on_l_system_clicked(self):
        """
        Open the L-system fractal type dialog.

        Instantiates the LSystemFractalTypeDialog with no parent window.
        """
        LSystemFractalTypeDialog(self)


def select_pattern_type_dialog(parent):
    """
    Open the "Select pattern type" dialog.

    Creates a PatternTypeDialog with no parent, opening the modal dialog that lets the user choose a pattern type.
    """
    PatternTypeDialog(parent)
