import json
import os
import uuid

from PySide6 import QtWidgets
from PySide6.QtCore import QPoint, Qt, QTimeLine, QLineF, Signal, QRectF, QPointF, QSizeF
from PySide6.QtGui import QColor, QPen, QPainter, QSurfaceFormat, QWheelEvent, QCursor, QDropEvent, QKeyEvent, \
    QTransform
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QGraphicsView, QFrame, QMenu, QGraphicsScene, QWidget, QGraphicsSceneMouseEvent, \
    QGraphicsProxyWidget, QLineEdit, QScrollArea

from App.Desktop.Win.Code.ui.NodeEditor.NodeLogic import NodeLogic
from App.Desktop.Win.Code.ui.NodeEditor.NodeSearchBar import NodeSearchBar
from App.Desktop.Win.Code.ui.NodeEditor.Nodes import Node, Pin, Connection, I_Node


class NodeWidget(QtWidgets.QWidget):
    def __init__(self, vega, parent):
        super().__init__(parent)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)

        self.node_editor = NodeLogic(self)
        self.scene = NodeScene(vega)
        self.scene.setSceneRect(0, 0, 9999, 9999)
        self.view = BlueprintView(vega, parent=self)
        self.view.setScene(self.scene)
        self.view.load_last_nodes()

        main_layout.addWidget(self.view)


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
        self.editor_w = NodeWidget(vega, self)

        # Filter
        searchbar = NodeSearchBar(self)
        self.splitter.addWidget(searchbar)
        self.splitter.addWidget(self.editor_w)
        lay.addWidget(self.splitter)

class BlueprintView(QGraphicsView):
    bg_color = QColor(38, 38, 38)
    grid_pen_s = QPen(QColor(52, 52, 52, 255), 0.5)
    grid_pen_l = QPen(QColor(22, 22, 22, 255), 1.0)

    grid_size_fine = 15
    grid_size_course = 150

    mouse_wheel_zoom_rate = 0.0015

    def __init__(self, vega, **kwargs):
        super().__init__(**kwargs)

        self.setRenderHint(QPainter.Antialiasing)
        self.vega = vega

        gl = QSurfaceFormat()
        gl.setSamples(10)
        QSurfaceFormat.setDefaultFormat(gl)
        gl_widget = QOpenGLWidget()
        self.setObjectName("BP_bg")
        self.setWindowTitle("Node in QGraphicsItem")
        # self.logic = NodeLogic(self)

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

    def get_node_by_uuid(self, u):
        for node in self.scene().items():
            if isinstance(node, Node):
                print(f"Checking {node.uuid} with {u}")
                if node.uuid == u:
                    return node

    def load_last_nodes(self):
        uuid_eq = {}
        nod_path = os.path.join(os.getenv("APPDATA"), ".vega", "nodes.veg")
        with os.scandir(os.path.join(os.getenv("APPDATA"), ".vega")) as scan:
            n = False
            for entry in scan:
                if entry.is_file() and entry.name.startswith("node"):
                    n = True
            if not n:
                with open(nod_path, "w") as f:
                    f.write("")
                    f.close()
        with open(nod_path, "r") as file:
            lines = "".join([line for line in file.readlines()])
            if len(lines) > 0:
                content = json.loads(lines)
                if content is not None and len(content.keys()) > 0:
                    for node_uuid, prop in content.get("Nodes").items():
                        uuid_eq.update({node_uuid: uuid.uuid4()})

                        ev = prop.get("event")
                        section = prop.get("itg")
                        element = prop.get("name")

                        if not section == "Vega":
                            if not ev:
                                method = self.vega.get_method_by_formal_name_and_itg(element, section, False)
                                node = Node(method.get("formal_name"), section, self.vega)
                                node.uuid = uuid_eq.get(node_uuid)
                                node.integration = section
                                node.id_name = element
                                node.set_function(method.get("func"))
                                # node.use_display = self.parentWidget().parent().vega.main_frame.canvaspanels[section] if method.get(
                                #     "use_display") else None
                                print(node.use_display)
                                node.execution_policy = method.get("exec_pol")
                                if method.get("node") == "exec":
                                    node.add_pin("in", True, False)
                                    if method.get("exec_pins"):
                                        for s_pìn in method.get("exec_pins"):
                                            node.add_pin(s_pìn, True, True)
                                    else:
                                        node.add_pin("out", True, True)
                                for name, type in method.get("inputs").items():
                                    # if node.use_display is None:
                                    #     node.add_pin(name, False, False, datatype=type)
                                    # else:
                                    #     if name != list(method.get("inputs").keys())[0]:
                                    #         node.add_pin(name, False, False, datatype=type)
                                    node.add_pin(name, False, False, datatype=type)
                                for name, type in method.get("outs").items():
                                    node.add_pin(name, False, True, datatype=type)
                            elif ev:

                                node = Node(element, section, self.vega)
                                node.uuid = uuid_eq.get(node_uuid)
                                node.add_pin("out", True, True)
                                node.event = True
                                node.integration = section
                                node.event_name = element
                                node.id_name = element
                                node.event_itg = section
                                for name, type in self.vega.events.get(section).get(element).items():
                                    node.add_pin(name, False, True, datatype=type)
                                self.vega.event_nodes.update({section: {element: node}})
                            node.build()
                            node.setPos(prop.get("pos")[0], prop.get("pos")[1])
                            self.scene().addItem(node)

                        else:
                            node = None
                            if element == "Int number":
                                node = I_Node("Int number", section, self.vega, data_type=int, node_color=[0, 122, 204])
                                node.add_pin("Value", False, True, datatype=int)
                                node.element.setText(str(prop.get("stablished_value")))
                            elif element == "Float number":
                                node = I_Node("Float number", section, self.vega, data_type=float, node_color=[0, 204, 0])
                                node.add_pin("Value", False, True, datatype=float)
                                node.element.setText(str(prop.get("stablished_value")))
                            elif element == "String text":
                                node = I_Node("String text", section, self.vega, data_type=str, node_color=[255, 26, 26])
                                node.add_pin("Value", False, True, datatype=str)
                                node.element.setText(prop.get("stablished_value"))
                            elif element == "Boolean":
                                node = I_Node("Boolean", section, self.vega, data_type=bool, node_color=[255, 153, 51])
                                node.add_pin("Value", False, True, datatype=bool)
                                node.element.setChecked(prop.get("stablished_value"))
                            node.uuid = uuid_eq.get(node_uuid)
                            node.integration = "Vega"
                            node.build()
                            node.setPos(prop.get("pos")[0], prop.get("pos")[1])
                            self.scene().addItem(node)

                    for node_uuid, prop in content.get("Nodes").items():
                        for pin_name, complementary in prop.get("out_pins").items():
                            for conn_uuid, end_pin_name in complementary.items():
                                conn = Connection()
                                conn.set_start_pin(self.get_node_by_uuid(uuid_eq.get(node_uuid)).get_pin(pin_name))
                                print(node_uuid)
                                conn.set_end_pin(self.get_node_by_uuid(uuid_eq.get(conn_uuid)).get_pin(end_pin_name))
                                self.scene().addItem(conn)
                                conn.updatePath()
                else:
                    del content
                    del uuid_eq
                file.close()

    def dropEvent(self, event: QDropEvent):
        section = event.mimeData().data("section").toStdString()
        element = event.mimeData().data("element").toStdString()
        ev = event.mimeData().data("event").toStdString()
        ev = ev == "True"

        if not section == "Vega":
            if not ev:
                method = self.vega.get_method_by_formal_name_and_itg(element, section, False)
                node = Node(method.get("formal_name"), section, self.vega)
                node.uuid = uuid.uuid4()
                node.id_name = element
                node.integration = section
                node.set_function(method.get("func"))
                node.use_display = self.parentWidget().parent().vega.main_frame.canvaspanels[section] if method.get(
                    "use_display") else None
                node.execution_policy = method.get("exec_pol")
                if method.get("node") == "exec":
                    node.add_pin("in", True, False)
                    if method.get("exec_pins"):
                        for s_pìn in method.get("exec_pins"):
                            node.add_pin(s_pìn, True, True)
                    else:
                        node.add_pin("out", True, True)
                for name, type in method.get("inputs").items():
                    # if node.use_display is None:
                    #     node.add_pin(name, False, False, datatype=type)
                    # else:
                    #     if name != list(method.get("inputs").keys())[0]:
                    #         node.add_pin(name, False, False, datatype=type)
                    node.add_pin(name, False, False, datatype=type)
                for name, type in method.get("outs").items():
                    node.add_pin(name, False, True, datatype=type)
                node.build()
                node.setPos(self.mapToScene(self.mapFromGlobal(QCursor.pos())))
                self.scene().addItem(node)
            elif ev:
                n = self.vega.get_event_node_by_name_and_itg(section, element)

                # CHECK NODES

                if not n:
                    node = Node(element, section, self.vega)
                    node.uuid = uuid.uuid4()
                    node.add_pin("out", True, True)
                    node.event = True
                    node.integration = section
                    node.event_name = element
                    node.id_name = element
                    node.event_itg = section
                    for name, type in self.vega.events.get(section).get(element).items():
                        node.add_pin(name, False, True, datatype=type)
                    self.vega.event_nodes.update({section: {element: node}})
                    node.build()
                    node.setPos(self.mapToScene(self.mapFromGlobal(QCursor.pos())))
                    self.scene().addItem(node)
                else:
                    # self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (event.x() - self.pan_start_x))
                    #
                    # self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (event.y() - self.pan_start_y))
                    self.horizontalScrollBar().setValue(self.mapFromScene(n.pos().x(), n.pos().y()).x())
                    self.verticalScrollBar().setValue(self.mapFromScene(n.pos().x(), n.pos().y()).y())
        else:
            node = None
            if element == "Int number":
                node = I_Node("Int number", section, self.vega, data_type=int, node_color=[0, 122, 204], sc=self.scene())
                node.add_pin("Value", False, True, datatype=int)
                node.sc = self.scene()
            elif element == "Float number":
                node = I_Node("Float number", section, self.vega, data_type=float, node_color=[0, 204, 0])
                node.add_pin("Value", False, True, datatype=float)
                node.sc = self.scene()
            elif element == "String text":
                node = I_Node("String text", section, self.vega, data_type=str, node_color=[255, 26, 26])
                node.add_pin("Value", False, True, datatype=str)
                node.sc = self.scene()
            elif element == "Boolean":
                node = I_Node("Boolean", section, self.vega, data_type=bool, node_color=[255, 153, 51])
                node.add_pin("Value", False, True, datatype=bool)
                node.sc = self.scene()
            node.uuid = uuid.uuid4()
            node.integration = "Vega"
            node.build()
            node.setPos(self.mapToScene(self.mapFromGlobal(QCursor.pos())))
            self.scene().addItem(node)
        super().dropEvent(event)

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

    def __init__(self, vega):
        super().__init__()
        self.setSceneRect(0, 0, 9999, 9999)
        self.event_nodes = []
        # vega.worker.signals.received_data.connect(self.process_event)
        self.last_node = None
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
                for con in item.connections:
                    con.delete()
            else:
                self.current_conn = Connection()
                self.addItem(self.current_conn)
                self.current_conn.set_start_pin(item)
                self.current_conn.end_pos = event.scenePos()
                self.current_conn.updatePath()
                return True

        if self.last_node:
            self.last_node.select_connections(False)
            super().mousePressEvent(event)

        if isinstance(item, Node):
            super().mousePressEvent(event)
            if self.last_node:
                self.last_node.setSelected(False)
            item.setSelected(True)
            item.allowMove = True
            item.select_connections(True)
            self.last_node = item
        else:
            if self.last_node:
                self.last_node.setSelected(False)
                self.last_node = None

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_Delete:
            for item in self.selectedItems():
                if isinstance(item, (Connection, Node)):
                    item.delete()
            return True
        elif event.key() == Qt.Key.Key_Alt:
            self.alt = True
            return True

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Alt:
            self.alt = False
            return True
        super().keyReleaseEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        super().mouseMoveEvent(event)
        if self.current_conn:
            self.current_conn.end_pos = event.scenePos()
            self.current_conn.updatePath()
            return True
        else:
            if self.last_node and self.last_node.allowMove:
                self.last_node.moveBy(event.scenePos().x() - self.last_node.scenePos().x(),
                                      event.scenePos().y() - self.last_node.scenePos().y())
                for pin in self.last_node.pins:
                    if pin.is_connected():
                        for con in pin.connections:
                            con.update_start_end_pos()
                            con.updatePath()

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        super().mouseReleaseEvent(event)
        item = self.itemAt(event.scenePos(), QTransform())
        if self.current_conn:
            if isinstance(item, Pin):
                if self.current_conn.start_pin.can_connect_to(item):
                    if item.is_connected() and not item.output:
                        item.connections[0].delete()
                    # self.current_conn.start_pin.clear_connection()
                    # item.clear_connection()
                    self.current_conn.set_end_pin(item)
                    self.current_conn.update_start_end_pos()
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

    def dropEvent(self, event):
        print("hello")