"""Implementation of 'Select fractal type' dialog."""

#
#  (C) Copyright 2019  Pavel Tisnovsky
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

        self.icon1=tkinter.PhotoImage(file="images/mandelbrot.png")
        self.icon2=tkinter.PhotoImage(file="images/mandelbrot_bw.png")

        n1=tkinter.Button(top_part)
        n1.config(text="In complex plane", image=self.icon2, compound=tkinter.TOP)
        n1.grid(row=0, column=1)

        n1.bind("<Enter>", lambda e:n1.config(image=self.icon1))
        n1.bind("<Leave>", lambda e:n1.config(image=self.icon2))

        # rest
        cancelButton = tkinter.Button(self, text="Cancel", command=self.cancel)
        cancelButton.grid(row=2, column=1, sticky="NWSE")

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # how the buttons should behave
        self.bind("<Escape>", lambda event: self.destroy())

    def cancel(self):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.wait_window()
        # return self.rooms, self.id.get()

def select_fractal_type_dialog():
    FractalTypeDialog(None)
