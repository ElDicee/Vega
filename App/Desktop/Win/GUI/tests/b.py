from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Switching Example")

        # Create a layout for the central widget
        layout = QVBoxLayout()

        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Create and add your different windows to the stacked widget
        window1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QPushButton("Switch to Window 2", clicked=self.switch_to_window2))
        window1.setLayout(layout1)
        self.stacked_widget.addWidget(window1)

        window2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QPushButton("Switch to Window 1", clicked=self.switch_to_window1))
        window2.setLayout(layout2)
        self.stacked_widget.addWidget(window2)

        # Add the stacked widget to the layout
        layout.addWidget(self.stacked_widget)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def switch_to_window1(self):
        self.stacked_widget.setCurrentIndex(0)

    def switch_to_window2(self):
        self.stacked_widget.setCurrentIndex(1)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
