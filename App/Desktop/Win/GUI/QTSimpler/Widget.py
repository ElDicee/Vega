from PyQt6.QtWidgets import QWidget, QHBoxLayout
import enum


class HBoxLayoutType(enum):
    HORIZONTAL = "horizontalLayout",
    VERTICAL = "verticalLayout"


def create_widget(objectname: str = "widget",
                  layout: HBoxLayoutType = None,
                  **kwargs):
    w = QWidget(parent=kwargs.get("parent"))
    w.setObjectName(objectname)
    if layout is not None:
        applyLayoutTo(w, layout)
    return w


def applyLayoutTo(w, layout, id: str = None):
    l = QHBoxLayout(w)
    l.setObjectName(f"{layout}{f'_{id}' if id is not None else ''}")

class LayeredWidget(QWidget):
    def __init__(self):
        super(LayeredWidget, self).__init__()
