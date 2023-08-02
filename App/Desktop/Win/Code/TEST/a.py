import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap

class ImageWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.initUI(image_path)

    def initUI(self, image_path):
        layout = QVBoxLayout()
        label = QLabel(self)

        # Load the image from the file using QPixmap
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            print(f"Failed to load the image from '{image_path}'")
            sys.exit(1)

        # Display the image in the label
        label.setPixmap(pixmap)
        layout.addWidget(label)
        self.setLayout(layout)

        self.setWindowTitle('Image Display')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_path = '../res/images/star-sky.jpg'  # Replace this with the path to your image file
    window = ImageWidget(image_path)
    sys.exit(app.exec())