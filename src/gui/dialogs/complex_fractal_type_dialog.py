"""Fractals in complex plane dialog."""

#
#  (C) Copyright 2019, 2026  Pavel Tisnovsky
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

from typing import Callable


class ComplexFractalTypeDialog(tkinter.Toplevel):

    def __init__(self, parent: tkinter.Tk) -> None:
        """
        Create a modal top-level dialog for selecting a fractal in the complex plane.

        Initializes the Toplevel window as a child of `parent`, builds the
        dialog's labeled frame and a Cancel button, binds the window close
        button and Escape key to close the dialog, and grabs focus to make the
        dialog modal.

        Parameters:
            parent (tkinter.Widget): Parent widget or window that owns this dialog.
        """
        tkinter.Toplevel.__init__(self, parent)
        top_part = tkinter.LabelFrame(
            self, text="Fractal in complex plane", padx=5, pady=5
        )
        top_part.grid(row=1, column=1, sticky="NWSE")

        _mandelbrot_button, mandelbrot_icons = self.fractal_button(
            top_part, "Mandelbrot", "mandelbrot", 0, 1, self.on_mandelbrot_clicked
        )
        _barnsley_button, barnsley_icons = self.fractal_button(
            top_part, "Barnsley", "barnsley1", 0, 2, self.on_barnsley_clicked
        )
        _magnet1_button, magnet1_icons = self.fractal_button(
            top_part, "Magnet1", "magnet1", 1, 1, self.on_magnet1_clicked
        )
        _magnet2_button, magnet2_icons = self.fractal_button(
            top_part, "Magnet2", "magnet2", 1, 2, self.on_magnet2_clicked
        )
        _newton_button, newton_icons = self.fractal_button(
            top_part, "Newton", "newton", 2, 1, self.on_newton_clicked
        )

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
        _mandelbrot_button.focus_set()

    def fractal_button(
        self,
        placement: tkinter.Widget,
        text: str,
        icon_name: str,
        row: int,
        column: int,
        command: Callable,
    ) -> tuple[tkinter.Widget, tuple[tkinter.PhotoImage, tkinter.PhotoImage]]:
        """
        Create and place a framed button for selecting a fractal type with hoverable icons.

        Parameters:
            placement: The parent tkinter widget or container where the button will be placed.
            text (str): Label displayed below the icon on the button.
            icon_name (str): Base name of the icon files located in the images/ directory (without suffix).
            row (int): Grid row index where the button will be placed.
            column (int): Grid column index where the button will be placed.
            command (callable): Callback invoked when the button is clicked.

        Returns:
            tuple: (button, icons) where `button` is the created tkinter.Button and `icons` is a two-tuple
            (color_photoimage, bw_photoimage) of tkinter.PhotoImage objects used for hover and default states.
        """
        icons = (
            tkinter.PhotoImage(file="images/cplx/" + icon_name + ".png"),
            tkinter.PhotoImage(file="images/cplx/" + icon_name + "_bw.png"),
        )

        button = tkinter.Button(placement, command=command)
        button.config(text=text, image=icons[1], compound=tkinter.TOP)
        button.grid(row=row, column=column)

        button.bind("<Enter>", lambda e: button.config(image=icons[0]))
        button.bind("<Leave>", lambda e: button.config(image=icons[1]))

        return button, icons

    def cancel(self) -> None:
        """
        Close the dialog window.

        Destroys the Toplevel window, closing the dialog and releasing its associated resources.
        """
        self.destroy()

    def show(self) -> None:
        """
        Display the dialog (restore if minimized) and block until the window is closed.

        This brings the dialog to the foreground if it was minimized and then
        waits for the dialog window to be destroyed, preventing code execution
        from continuing until the user closes the dialog.
        """
        self.wm_deiconify()
        self.wait_window()

    def on_mandelbrot_clicked(self) -> None:
        pass

    def on_barnsley_clicked(self) -> None:
        pass

    def on_magnet1_clicked(self) -> None:
        pass

    def on_magnet2_clicked(self) -> None:
        pass

    def on_newton_clicked(self) -> None:
        pass
