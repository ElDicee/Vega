import sys
from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import QApplication, QGraphicsItem, QGraphicsView, QGraphicsScene

class Node(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

        self.radius = 20
        self.color = QColor(100, 100, 200)

    def boundingRect(self):
        adjust = self.radius + 2
        return QRectF(-adjust, -adjust, 2 * adjust, 2 * adjust)

    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            # Restrict the node within the scene boundaries
            newPos = value
            sceneRect = self.scene().sceneRect()
            newPos.setX(min(sceneRect.right(), max(newPos.x(), sceneRect.left())))
            newPos.setY(min(sceneRect.bottom(), max(newPos.y(), sceneRect.top())))
            return newPos
        return super().itemChange(change, value)

class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setScene(QGraphicsScene(self))
        self.setSceneRect(-200, -200, 400, 400)

        node = Node()
        self.scene().addItem(node)
        node.setPos(0, 0)

        self.setWindowTitle("Node Example")
        self.show()

def main():
    app = QApplication(sys.argv)
    view = GraphicsView()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
