from gui.main_window import MainWindow
from configuration import Configuration

configuration = Configuration()

mainWindow = MainWindow(configuration)
mainWindow.show()
