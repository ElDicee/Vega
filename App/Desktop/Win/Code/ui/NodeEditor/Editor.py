import uuid

from PySide6 import QtWidgets
from PySide6.QtCore import QPoint, Qt, QTimeLine, QLineF, Signal, QRectF, QPointF, QSizeF
from PySide6.QtGui import QColor, QPen, QPainter, QSurfaceFormat, QWheelEvent, QCursor, QDropEvent, QKeyEvent, \
    QTransform
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QGraphicsView, QFrame, QMenu, QGraphicsScene, QWidget, QGraphicsSceneMouseEvent

from App.Desktop.Win.Code.ui.NodeEditor.NodeLogic import NodeLogic
from App.Desktop.Win.Code.ui.NodeEditor.NodeSearchBar import NodeSearchBar
from App.Desktop.Win.Code.ui.NodeEditor.Nodes import Node, Pin, Connection


class EditorWidget(QWidget):
    def __init__(self, vega):
        super().__init__()
        self.vega = vega
        self.setStyleSheet("border: solid 2px rgba(0,0,0,0); border-radius: 10px;")
        lay = QtWidgets.QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setStyleSheet("QSplitter{background-color: rgba(0,0,0,0)}")

        self.view = BlueprintView(vega)
        # Filter
        searchbar = NodeSearchBar(self)

        self.splitter.addWidget(searchbar)
        self.splitter.addWidget(self.view)

        lay.addWidget(self.splitter)


class BlueprintView(QGraphicsView):
    bg_color = QColor(38, 38, 38)
    grid_pen_s = QPen(QColor(52, 52, 52, 255), 0.5)
    grid_pen_l = QPen(QColor(22, 22, 22, 255), 1.0)

    grid_size_fine = 15
    grid_size_course = 150

    mouse_wheel_zoom_rate = 0.0015

    def __init__(self, vega):
        super().__init__()

        self.setRenderHint(QPainter.Antialiasing)
        self.vega = vega

        gl = QSurfaceFormat()
        gl.setSamples(10)
        QSurfaceFormat.setDefaultFormat(gl)
        gl_widget = QOpenGLWidget()
        self.setObjectName("BP_bg")
        self.setWindowTitle("Node in QGraphicsItem")
        self.logic = NodeLogic(self)

        self.currentscale = 1
        self.pan = False
        self.pan_start_x = 0
        self.pan_start_y = 0
        self.scalings = 0
        self.lastMousePos = QPoint()

        self.setViewport(gl_widget)

        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.Shape.NoFrame)

        self.setScene(NodeScene())
        # self.logic.install(self.scene())

    def wheelEvent(self, event: QWheelEvent):

        if self.pan:
            return

        degrees = event.angleDelta() / 8.0
        steps = degrees.y() / 5.0
        self.scalings += steps

        if self.scalings * steps < 0:
            self.scalings = steps

        self.anim = QTimeLine(350)
        self.anim.setUpdateInterval(20)
        self.anim.valueChanged.connect(self.scaling_time)
        self.anim.finished.connect(self.anim_finished)
        self.anim.start()

    def dropEvent(self, event: QDropEvent):
        section = event.mimeData().data("section").toStdString()
        element = event.mimeData().data("element").toStdString()
        method = self.vega.integrations.get(section).methods.get(element)
        print(method)
        node = Node(method.get("formal_name"), section)
        node.set_function(method.get("func"))
        if method.get("node") == "exec":
            node.add_pin("in", True, False)
            node.add_pin("out", True, True)
        elif method.get("node") == "event":
            node.add_pin("out", True, True)
        for name, type in method.get("inputs").items():
            node.add_pin(name, False, False, datatype=type)
        for name, type in method.get("outs").items():
            node.add_pin(name, False, True, datatype=type)

        node.build()
        node.uuid = uuid.uuid4()
        node.setPos(self.mapToScene(self.mapFromGlobal(QCursor.pos())))
        self.scene().addItem(node)

    def scaling_time(self, x):
        f = 1.0 + self.scalings / 300.0

        self.currentscale *= f

        self.scale(f, f)

    def anim_finished(self):

        if self.scalings > 0:
            self.scalings -= 1
        else:
            self.scalings += 1

    def drawBackground(self, painter, rect):
        painter.fillRect(rect, self.bg_color)

        left = int(rect.left()) - (int(rect.left()) % self.grid_size_fine)
        top = int(rect.top()) - (int(rect.top()) % self.grid_size_fine)

        gridLines = []
        painter.setPen(self.grid_pen_s)
        y = float(top)
        while y < float(rect.bottom()):
            gridLines.append(QLineF(rect.left(), y, rect.right(), y))
            y += self.grid_size_fine
        painter.drawLines(gridLines)

        gridLines = []
        painter.setPen(self.grid_pen_s)
        x = float(left)
        while x < float(rect.right()):
            gridLines.append(QLineF(x, rect.top(), x, rect.bottom()))
            x += self.grid_size_fine
        painter.drawLines(gridLines)

        left = int(rect.left()) - (int(rect.left()) % self.grid_size_course)
        top = int(rect.top()) - (int(rect.top()) % self.grid_size_course)

        gridLines = []
        painter.setPen(self.grid_pen_l)
        x = left
        while x < rect.right():
            gridLines.append(QLineF(x, rect.top(), x, rect.bottom()))
            x += self.grid_size_course
        painter.drawLines(gridLines)

        gridLines = []
        painter.setPen(self.grid_pen_l)
        y = top
        while y < rect.bottom():
            gridLines.append(QLineF(rect.left(), y, rect.right(), y))
            y += self.grid_size_course
        painter.drawLines(gridLines)

        return super().drawBackground(painter, rect)

    def mousePressEvent(self, event):
        """
        This method is called when a mouse press event occurs in the view. It sets the cursor to a closed hand cursor and
        enables panning if the middle mouse button is pressed.
        """
        if event.button() == Qt.MiddleButton:
            self.pan = True
            self.pan_start_x = event.x()
            self.pan_start_y = event.y()
            self.setCursor(Qt.ClosedHandCursor)

        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        This method is called when a mouse release event occurs in the view. It sets the cursor back to the arrow cursor and
        disables panning if the middle mouse button is released.
        """
        if event.button() == Qt.MiddleButton:
            self.pan = False
            self.setCursor(Qt.ArrowCursor)

        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        """
        This method is called when a mouse move event occurs in the view. It pans the view if the middle mouse button is
        pressed and moves the mouse.
        """
        if self.pan:
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (event.x() - self.pan_start_x))

            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (event.y() - self.pan_start_y))

            self.pan_start_x = event.x()
            self.pan_start_y = event.y()

        return super().mouseMoveEvent(event)


class NodeScene(QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 9999, 9999)
        self.event_nodes = []
        self.last_node:Node = None
        self.current_conn = None
        self.alt = False

    # def dragEnterEvent(self, e):
    #     e.acceptProposedAction()

    # def dropEvent(self, e):
    #     # find item at these coordinates
    #     item = self.itemAt(e.scenePos())
    #     if item.setAcceptDrops:
    #         item.dropEvent(e)

    def dragMoveEvent(self, e):
        e.acceptProposedAction()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        item = self.itemAt(event.scenePos(), QTransform())

        if isinstance(item, Pin):
            if self.alt:
                item.connection.delete()
            else:
                self.current_conn = Connection()
                self.addItem(self.current_conn)
                self.current_conn.start_pin = item
                self.current_conn.start_pos = item.scenePos()
                self.current_conn.end_pos = event.scenePos()
                self.current_conn.updatePath()
                return True

        if self.last_node:
            self.last_node.select_connections(False)

        if isinstance(item, Node):
            if self.last_node:
                self.last_node.setSelected(False)
            item.setSelected(True)
            item.allowMove = True
            item.select_connections(True)
            self.last_node = item
        else:
            self.last_node.setSelected(False)
            self.last_node = None

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Delete:
            for item in self.selectedItems():
                if isinstance(item, (Connection, Node)):
                    item.delete()
            return True
        elif event.key() == Qt.Key.Key_Alt:
            self.alt = True

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Alt:
            self.alt = False
            return True

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if self.current_conn:
            self.current_conn.end_pos = event.scenePos()
            self.current_conn.updatePath()
            return True
        else:
            if self.last_node and self.last_node.allowMove:
                self.last_node.moveBy(event.scenePos().x()-self.last_node.scenePos().x(), event.scenePos().y()-self.last_node.scenePos().y())

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        item = self.itemAt(event.scenePos(), QTransform())
        if self.current_conn:
            if isinstance(item, Pin):
                if self.current_conn.start_pin.can_connect_to(item):
                    if item.connection:
                        item.connection.delete()
                    self.current_conn.start_pin.clear_connection()
                    item.clear_connection()
                    self.current_conn.set_end_pin(item)
                    #self.current_conn.update_start_end_pos()
                else:
                    print("cant connect")
                    self.current_conn.delete()
                self.current_conn = None

            if self.current_conn:
                self.current_conn.delete()
                self.current_conn = None
                return True
        else:
            if isinstance(item, Node):
                if item.allowMove:
                    item.allowMove = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    launcher = EditorWidget()
    launcher.show()
    app.exec()
    sys.exit()
