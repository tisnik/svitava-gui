"""Toolbar displayed on the main windo."""

import tkinter

from gui.tooltip import Tooltip
from gui.dialogs.fractal_type_dialog import select_fractal_type_dialog
from gui.dialogs.pattern_type_dialog import select_pattern_type_dialog
from gui.dialogs.settings_dialog import settings_dialog

from configuration import Configuration


class Toolbar(tkinter.LabelFrame):
    """Toolbar displayed on the main window."""

    def __init__(
        self, parent: tkinter.Tk, main_window, icons, configuration: Configuration
    ) -> None:
        """
        Create and configure the toolbar frame and its widgets for the given main window.

        Initializes the LabelFrame labeled "Tools", creates the project load button with its icon and tooltip, adds a spacer, and arranges these widgets using the grid geometry manager.

        Parameters:
            main_window: The application main window object that provides UI resources (for example, icon references) used by toolbar widgets.
        """
        super().__init__(
            parent, text="Tools", padx=5, pady=5, font=("", configuration.gui_font_size)
        )

        self.parent = parent
        self.icons = icons
        self.main_window = main_window

        self.button_project_load = tkinter.Button(
            self,
            text="Load project",
            image=icons.file_open_icon,
            command=None,
        )
        Tooltip(self.button_project_load, "Load project")

        self.button_project_save = tkinter.Button(
            self,
            text="Save project",
            image=icons.file_save_icon,
            command=None,
        )
        Tooltip(self.button_project_save, "Save project")

        self.button_new_fractal = tkinter.Button(
            self,
            text="New fractal",
            image=icons.fractal_new_icon,
            command=self.command_fractal_type_dialog,
        )
        Tooltip(self.button_new_fractal, "New fractal")

        self.button_new_pattern = tkinter.Button(
            self,
            text="New pattern",
            image=icons.pattern_new_icon,
            command=self.command_pattern_type_dialog,
        )
        Tooltip(self.button_new_pattern, "New pattern")

        self.button_new_filter = tkinter.Button(
            self,
            text="New filter",
            image=icons.filter_new_icon,
            command=None,
        )
        Tooltip(self.button_new_filter, "New filter")

        self.button_new_color_mapper = tkinter.Button(
            self,
            text="New color mapper",
            image=icons.fill_color_icon,
            command=None,
        )
        Tooltip(self.button_new_color_mapper, "New color mapper")

        self.button_new_connection = tkinter.Button(
            self,
            text="New connection",
            image=icons.draw_arrow_forward_icon,
            command=None,
        )
        Tooltip(self.button_new_connection, "New connection")

        self.button_palette_editor = tkinter.Button(
            self,
            text="Palette editor",
            image=icons.edit_icon,
            command=None,
        )
        Tooltip(self.button_palette_editor, "Palette editor")

        self.button_settings = tkinter.Button(
            self,
            text="Settings",
            image=icons.configure_icon,
            command=self.settings_dialog,
        )
        Tooltip(self.button_settings, "Settings")

        self.button_quit = tkinter.Button(
            self,
            text="Quit",
            image=icons.exit_icon,
            command=parent.quit,
        )
        Tooltip(self.button_quit, "Quit")

        spacer1 = tkinter.Label(self, text="   ")
        spacer2 = tkinter.Label(self, text="   ")
        spacer3 = tkinter.Label(self, text="   ")
        spacer4 = tkinter.Label(self, text="   ")
        spacer5 = tkinter.Label(self, text="   ")
        spacer6 = tkinter.Label(self, text="   ")

        self.button_project_load.grid(column=1, row=1)
        self.button_project_save.grid(column=2, row=1)
        spacer1.grid(column=3, row=1)
        self.button_new_fractal.grid(column=4, row=1)
        self.button_new_pattern.grid(column=5, row=1)
        spacer2.grid(column=6, row=1)
        self.button_new_filter.grid(column=7, row=1)
        self.button_new_color_mapper.grid(column=8, row=1)
        spacer3.grid(column=9, row=1)
        self.button_new_connection.grid(column=10, row=1)
        spacer4.grid(column=11, row=1)
        self.button_palette_editor.grid(column=12, row=1)
        spacer5.grid(column=13, row=1)
        self.button_settings.grid(column=14, row=1)
        spacer6.grid(column=15, row=1)
        self.button_quit.grid(column=16, row=1)

    @staticmethod
    def disable_button(button) -> None:
        """
        Disable a Tkinter button widget by setting its state to "disabled".

        Parameters:
            button (tkinter.Button): The button widget to disable.
        """
        button["state"] = "disabled"

    @staticmethod
    def enable_button(button: tkinter.Button) -> None:
        """
        Enable the given Tkinter button widget.

        Parameters:
            button (tkinter.Button): The button widget to enable; its state will be set to "normal".
        """
        button["state"] = "normal"

    def command_fractal_type_dialog(self):
        """
        Open the fractal-type selection dialog.

        Displays the dialog that lets the user choose a fractal type to create.
        """
        select_fractal_type_dialog(self.parent, self.icons)

    def command_pattern_type_dialog(self):
        """
        Open the pattern selection dialog.

        Displays the dialog that lets the user choose a pattern type to create.
        """
        select_pattern_type_dialog(self.parent)

    def settings_dialog(self):
        """
        Open the settings dialog.

        Displays the dialog with configuration/settings.
        """
        settings_dialog(self.parent)
