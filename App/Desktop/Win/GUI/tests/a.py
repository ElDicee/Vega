import sys
from PyQt6.QtCore import Qt, QPoint, QPropertyAnimation, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class AnimationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPropertyAnimation Example")

        # Create a label for the animation
        self.label = QLabel(self)
        self.label.setText("Animation")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("QLabel { background-color: red; color: white; }")

        # Set the initial position
        self.label.move(0, 100)

        # Create a QPropertyAnimation for the label's position
        self.animation = QPropertyAnimation(self.label, b"pos")

        # Set the duration and end value of the animation
        self.animation.setDuration(2000)  # Animation duration in milliseconds
        self.animation.setEndValue(QPoint(810, 100))  # End position of the label

        # Start the animation
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec())
