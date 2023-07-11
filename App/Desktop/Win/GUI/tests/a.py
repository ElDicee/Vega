import sys

from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView

class TV(QTreeView):
    def __init__(self):
        super(TV, self).__init__()
        self.model = QFileSystemModel()
        self.model.setRootPath("")  # Set the root path for the file explorer

        # Create the QTreeView
        self.setModel(self.model)
        self.setRootIndex(self.model.index(""))  # Set the root index for the tree view
        self.setColumnWidth(0, 250)  # Set the width of the first column



class FileExplorerBrowsingTreeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)
        # Create a QFileSystemModel
        self.setCentralWidget(TV())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorerBrowsingTreeWindow()
    window.show()
    sys.exit(app.exec())