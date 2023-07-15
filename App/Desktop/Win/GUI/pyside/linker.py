from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
import sys
import ok_ui as tester

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    Form.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    Form.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    inst = tester.Ui_MainWindow()
    inst.setupUi(Form)
    Form.show()
    sys.exit(app.exec())