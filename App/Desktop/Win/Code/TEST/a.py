from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGraphicsScene, QGraphicsView, \
    QGraphicsProxyWidget
from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor


class App(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.button = QPushButton('Hello World')
        self.button.setGeometry(QRectF(0, 0, 100, 30))
        self.button.clicked.connect(self.button_clicked)

        self.layout.addWidget(self.button)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.layout.addWidget(self.view)

        self.button2 = QPushButton('Hello Scene')
        self.button2.setGeometry(QRectF(0, 0, 100, 30))
        self.button2.clicked.connect(self.button2_clicked)

        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(self.button2)
        self.scene.addItem(self.proxy)

        self.window.setLayout(self.layout)
        self.window.show()

    def button_clicked(self):
        print('Button 1 clicked')

    def button2_clicked(self):
        print('Button 2 clicked')


App()
