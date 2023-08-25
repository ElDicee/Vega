import sys

from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QGraphicsItem, QGraphicsProxyWidget, QGraphicsScene, QGraphicsView, QWidget
from PySide6.QtCore import Qt, QRectF

from App.Desktop.Win.Code.ui.Elements.Node import NodeType, Node


class NodeGraphicsItem(QGraphicsItem):
    def __init__(self, node=None):
        super().__init__()

        self.node_widget = Node(name="MyNode", node_type=NodeType.EXECUTION)
        if node is not None:
            self.node_widget = node# Crea una instancia de Node

        self.node_proxy = QGraphicsProxyWidget(self)
        self.node_proxy.setWidget(self.node_widget)
        self.node_proxy.setFlag(QGraphicsItem.ItemIsSelectable)
        self.node_proxy.setFlag(QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return self.node_proxy.boundingRect()

    def paint(self, painter, option, widget):
        pass

    def mousePressEvent(self, event):
        print("click")
        self.node_widget.mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.node_widget.mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        print("a")
        self.node_widget.mouseMoveEvent(event)



def main():
    app = QApplication(sys.argv)
    scene = QGraphicsScene()

    view = QGraphicsView(scene)
    view.setWindowTitle("Node in QGraphicsItem")
    view.setRenderHint(QPainter.Antialiasing)

    node_item = NodeGraphicsItem()
    node_item.setPos(100, 100)  # Establecer posición

    scene.addItem(node_item)

    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
