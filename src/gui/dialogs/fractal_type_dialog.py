"""Implementation of 'Select fractal type' dialog."""

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

from tkinter import messagebox


class FractalTypeDialog(tkinter.Toplevel):

    def __init__(self, parent):
        tkinter.Toplevel.__init__(self, parent)
        top_part = tkinter.LabelFrame(self, text="Fractal type", padx=5, pady=5)
        top_part.grid(row=1, column=1, sticky="NWSE")

        cplx_button, cplx_icons = self.fractal_button(top_part, "In complex plane", "mandelbrot")

        # rest
        cancelButton = tkinter.Button(self, text="Cancel", command=self.cancel)
        cancelButton.grid(row=2, column=1, sticky="NWSE")

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # how the buttons should behave
        self.bind("<Escape>", lambda event: self.destroy())

        self.grab_set()

    def fractal_button(self, placement, text, icon_name):
        icons = (
            tkinter.PhotoImage(file="images/" + icon_name + ".png"),
            tkinter.PhotoImage(file="images/" + icon_name + "_bw.png")
        )

        button = tkinter.Button(placement)
        button.config(text=text, image=icons[1], compound=tkinter.TOP)
        button.grid(row=0, column=1)

        button.bind("<Enter>", lambda e:button.config(image=icons[0]))
        button.bind("<Leave>", lambda e:button.config(image=icons[1]))

        return button, icons

    def cancel(self):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.wait_window()
        # return self.rooms, self.id.get()

def select_fractal_type_dialog():
    FractalTypeDialog(None)
