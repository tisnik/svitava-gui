"""Menu bar displayed on the main window."""

import tkinter

from gui.dialogs.about_dialog import about
from gui.dialogs.help_dialog import help
from gui.dialogs.fractal_type_dialog import select_fractal_type_dialog
from gui.dialogs.pattern_type_dialog import select_pattern_type_dialog
from gui.dialogs.filter_type_dialog import select_filter_type_dialog
from gui.dialogs.color_mapper_dialog import select_color_mapper_dialog
from gui.dialogs.settings_dialog import settings_dialog

from configuration import Configuration



class Menubar(tkinter.Menu):
    """Menu bar displayed on the main window."""

    def __init__(self, parent, main_window, icons, configuration: Configuration):
        """
        Create and populate the application's top-level menu bar and bind its keyboard shortcuts.
        
        Parameters:
        	parent (tkinter.Tk or tkinter.Widget): The root or parent widget to attach the menu to and register key bindings on.
        	main_window (object): Application main window providing resources used by the menus (for example `icons`) and callbacks.
        """
        super().__init__(tearoff=0)

        main_menu_font = font = ("", configuration.main_menu_font_size)
        menu_font = font = ("", configuration.menu_font_size)

        self.parent = parent
        self.icons = icons
        self.main_window = main_window

        self.file_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.file_menu.add_command(label="Load project", image=icons.file_open_icon,
                                    compound="left", underline=0, accelerator="Ctrl+L")
        self.file_menu.add_command(label="Save project", image=icons.file_save_icon,
                                    compound="left", underline=0, accelerator="Ctrl+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", image=icons.exit_icon,
                                  compound="left", underline=0, accelerator="Ctrl+Q",
                                  command=parent.quit)

        self.renderer_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.renderer_menu.add_command(label="New fractal", image=icons.fractal_new_icon,
                                     compound="left", underline=0, accelerator="Ctrl+N",
                                     command=self.command_fractal_type_dialog)
        self.renderer_menu.add_separator()
        self.renderer_menu.add_command(label="New pattern", image=icons.pattern_new_icon,
                                     compound="left", underline=0, accelerator="Ctrl+P",
                                     command=self.command_pattern_type_dialog)

        self.processor_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.processor_menu.add_command(label="New filter", image=icons.filter_new_icon,
                                     compound="left", underline=4, accelerator="Ctrl+F",
                                     command=self.command_filter_type_dialog)
        self.processor_menu.add_separator()
        self.processor_menu.add_command(label="New color mapper", image=icons.fill_color_icon,
                                     compound="left", underline=4, accelerator="Ctrl+C",
                                     command=self.command_color_mapper_dialog)

        self.compositor_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.compositor_menu.add_command(label="New connection", image=icons.draw_arrow_forward_icon,
                                     compound="left", underline=4, accelerator="Ctrl+A",
                                     command=None)

        self.palette_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.palette_menu.add_command(label="Load palette", image=icons.file_open_icon,
                                    compound="left", underline=0)
        self.palette_menu.add_command(label="Save palette", image=icons.file_save_icon,
                                    compound="left", underline=0)
        self.palette_menu.add_command(label="Palette editor", image=icons.edit_icon,
                                    compound="left", underline=0)

        self.settings_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.settings_menu.add_command(label="Configuration",
                                  image=icons.configure_icon,
                                  compound="left", underline=0, accelerator="F9",
                                  command=self.settings_dialog)

        self.help_menu = tkinter.Menu(self, tearoff=0, font=menu_font)
        self.help_menu.add_command(label="Help",
                                  image=icons.help_faq_icon,
                                  compound="left", underline=0, accelerator="F1",
                                  command=help)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="About",
                                  image=icons.help_about_icon, accelerator="F11",
                                  compound="left", underline=0, command=about)

        self.add_cascade(label="File", menu=self.file_menu, underline=0, font = main_menu_font)
        self.add_cascade(label="Renderer", menu=self.renderer_menu, underline=0, font = main_menu_font)
        self.add_cascade(label="Processor", menu=self.processor_menu, underline=0, font = main_menu_font)
        self.add_cascade(label="Compositor", menu=self.compositor_menu, underline=0, font = main_menu_font)
        self.add_cascade(label="Palette", menu=self.palette_menu, underline=1, font = main_menu_font)
        self.add_cascade(label="Settings", menu=self.settings_menu, underline=0, font = main_menu_font)
        self.add_cascade(label="Help", menu=self.help_menu, underline=0, font = main_menu_font)

        self.parent.bind('<F1>', lambda event: help())
        self.parent.bind('<F11>', lambda event: about())
        self.parent.bind('<Control-n>', lambda event: self.command_fractal_type_dialog())

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

    def command_filter_type_dialog(self):
        """
        Open the filter selection dialog.
        
        Displays the dialog that lets the user choose a filter type to create.
        """
        select_filter_type_dialog(self.parent)

    def command_color_mapper_dialog(self):
        """
        Open the color mapper selection dialog.
        
        Displays the dialog that lets the user choose a color mapper to create.
        """
        select_color_mapper_dialog(self.parent)

    def settings_dialog(self):
        """
        Open the settings dialog.
        
        Displays the dialog with configuration/settings.
        """
        settings_dialog(self.parent)
