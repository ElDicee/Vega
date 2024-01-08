import integrations.VegaAPI as api
from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot
import numpy as np


def init_video_capture(cam_num: int):
    return cv2.VideoCapture(cam_num)


def read_from_capture(cap):
    return cap.read()


def convert_cv_qt(image_width, image_height, cv_img):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    rgb_image = cv2.flip(rgb_image, 1)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(image_width, image_height, Qt.KeepAspectRatio)
    return QPixmap.fromImage(p)


def shutdown_video_capture(capture):
    capture.release()

class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class App(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Webcam')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        # self.thread = VideoThread()
        # # connect its signal to the update_image slot
        # self.thread.change_pixmap_signal.connect(self.update_image)
        # # start the thread
        # self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_image(self, img):
        """Updates the image_label with a new opencv image"""
        self.image_label.setPixmap(img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())


def vega_main():
    w = App()
    vega = api.Vega_Portal()
    vega.set_name("OpenCV ITG")
    vega.add_display_screen(w)
    vega.add_method(api.Method(init_video_capture, api.EXECUTION, outputs={"Capture": None}, formal_name="WebcapCapture Instance"))
    vega.add_method(api.Method(read_from_capture, api.OPERATOR, outputs={"Result": bool, "Image": None}, formal_name="Read Image from Capture"))
    vega.add_method(api.Method(read_from_capture, api.OPERATOR, outputs={"Result": bool, "Image": None}, formal_name="Read Capture Image"))
    vega.add_method(api.Method(shutdown_video_capture, api.EXECUTION, formal_name="Shutdown Video Capture"))
    vega.add_method(api.Method(convert_cv_qt, api.OPERATOR, outputs={"Qt Pixmap": None}, formal_name="CV2 Img to Qt Pixmap"))
    vega.add_method(api.Method(w.update_image, api.EXECUTION, formal_name="Update Display Image"))
    return vega
