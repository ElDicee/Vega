import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt6.QtCore import QDir, QSortFilterProxyModel, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon

class FolderFilterProxyModel(QSortFilterProxyModel):
    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        if index.isValid():
            file_info = index.data(Qt.ItemDataRole.UserRole)
            return file_info.isDir()
        return False

class FileExplorerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)

        # Create a QStandardItemModel
        self.model = QStandardItemModel()

        # Create the QSortFilterProxyModel
        self.proxy_model = FolderFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Create the QTreeView
        self.tree_view = QTreeView(self)
        self.tree_view.setModel(self.proxy_model)
        self.tree_view.setRootIndex(self.model.invisibleRootItem().index())

        self.setCentralWidget(self.tree_view)

        # Load directory
        self.load_directory(QDir.rootPath())

    def load_directory(self, path):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([path])

        root_item = self.model.invisibleRootItem()
        self.add_directory(root_item, path)

    def add_directory(self, parent_item, path):
        dir_entries = QDir(path).entryInfoList(
            QDir.Filter.AllDirs | QDir.Filter.NoDotAndDotDot | QDir.Filter.Hidden
        )

        for entry in dir_entries:
            dir_item = QStandardItem(entry.fileName())
            dir_item.setData(entry, Qt.ItemDataRole.UserRole)
            dir_item.setIcon(QIcon.fromTheme("folder"))  # Use the folder icon
            parent_item.appendRow(dir_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorerWindow()
    window.show()
    sys.exit(app.exec())
