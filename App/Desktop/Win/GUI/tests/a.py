import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QStyle
from PyQt6.QtCore import QDir, QSortFilterProxyModel, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class FileExplorerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)

        # Crear el modelo de datos
        self.model = QStandardItemModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Crear la vista del árbol
        self.tree_view = QTreeView(self)
        self.tree_view.setModel(self.proxy_model)
        self.tree_view.setRootIsDecorated(True)

        # Establecer la ruta raíz
        self.root_path = QDir.rootPath()
        self.load_directory(self.root_path)

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
            dir_item.setData(entry.filePath(), Qt.ItemDataRole.UserRole)  # Use Qt.ItemDataRole.UserRole
            dir_item.setIcon(self.tree_view.style().standardIcon(QStyle.StandardPixmap.SP_DirIcon))  # Use QStyle.StandardPixmap.SP_DirIcon
            parent_item.appendRow(dir_item)

    def set_filter(self, text):
        self.proxy_model.setFilterFixedString(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorerWindow()
    window.show()
    sys.exit(app.exec())
