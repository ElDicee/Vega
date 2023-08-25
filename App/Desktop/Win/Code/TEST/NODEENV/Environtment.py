import enum

from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsSceneHoverEvent, \
    QGraphicsSceneMouseEvent
import json
import uuid

CONST_PIN_HEIGHT = 12
CONST_SPACE_BETWEEN_PINS = 10


class NodeType(enum.Enum):
    EXECUTION = "exec"
    OPERATOR = "oper"


class PinType(enum.Enum):
    INPUT_PIN = "in"
    OUTPUT_PIN = "out"
    EXEC_FLOW_PIN = "exec"

    def valueOf(name):
        return NodeType.EXECUTION if name == "exec" else NodeType.OPERATOR


def saveNodes(nodes):
    d = {}
    for node in nodes:
        d.update({node.id: {
            "itg": None,
            "method": None,
            "pos": [node.pos().x().real, node.pos().y().real]
        }})
        for pin in node.output_pins:
            d.get(node.id).update({"linkers": [
                {
                    "id": pin.linked_inp.p.id,
                    "input_valuename": pin.linked_inp.valuename
                }
            ]})


class Pin(QGraphicsItem):
    def __init__(self, p, pintype: PinType = PinType.INPUT_PIN, valuename: str = "Value", datatype=object, **kwargs):
        super().__init__()
        self.radius = 5
        self.p = p  # PARENT
        self.relative_location = [0, 0]
        self.bg_color = [255, 0, 0, 255]
        self.setAcceptHoverEvents(True)
        self.pintype = pintype
        self.valuename = valuename
        self.datatype = datatype
        self.defRelPos(0, 3)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, False)

    def boundingRect(self) -> QRectF:
        return QRectF(self.pos().x().real, self.pos().y().real, CONST_PIN_HEIGHT, CONST_PIN_HEIGHT)

    def defRelPos(self, x, y):
        self.setPos(self.p.pos().x().real + x, self.p.pos().y().real + y)

    def getRelPos(self):
        return [self.pos().x() - self.p.pos().x(), self.pos().y() - self.p.pos().y()]

    def paint(self, painter: QPainter, option, widget=None):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(
            QPen(Qt.GlobalColor.darkGray, 0, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
        painter.setBrush(QColor(self.bg_color[0], self.bg_color[1], self.bg_color[2], self.bg_color[3]))
        painter.drawRoundedRect(self.boundingRect(), 3, 3)
        painter.drawText(QPointF(self.pos().x() + CONST_PIN_HEIGHT + 5, self.pos().y()+2*CONST_PIN_HEIGHT/3), self.valuename)

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent):
        self.bg_color = [0, 255, 0, 255]
        self.update()

    def hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent):
        self.bg_color = [255, 0, 0, 255]
        self.update()

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        pass


class Node(QGraphicsItem):
    def __init__(self, scene, name: str, node_type: NodeType, **kwargs):
        super().__init__()
        scene.addItem(self)
        self.input_pins = {}
        self.output_pins = {}
        self.ch = []
        self.function = None
        self.name = name
        self.node_type = node_type
        self.formal_name = self.name
        self.size = [40, 45]
        self.id = uuid.uuid4()

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)

        if kwargs.get("formal_name"):
            self.formal_name = kwargs.get("formal_name")
        self.add_input_pin("jorge", str)
        self.add_input_pin("juan", str)
        self.add_input_pin("a", str)
        self.add_input_pin("b", str)
        self.add_input_pin("juasdgadsgdsafagdsdgasdn", str)

    def paint(self, painter: QPainter, option, widget=None):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(QColor(255, 0, 0, 100))
        painter.drawRoundedRect(self.boundingRect(), 20, 3)

    def mov(self, x, y):
        self.setPos(QPointF(x, y))

    def boundingRect(self) -> QRectF:
        return QRectF(self.pos().x(), self.pos().y(), self.size[0], self.size[1])

    def adjustBlockSize(self):
        input_ = max([len(x) for x in self.input_pins.keys()]) if len(self.input_pins.keys()) > 0 else 0
        output_ = max([len(x) for x in self.output_pins.keys()]) if len(self.output_pins.keys()) > 0 else 0
        self.size[0] = 20+7*max(len(self.formal_name), input_+output_)
        self.size[1] = (CONST_SPACE_BETWEEN_PINS+CONST_PIN_HEIGHT)*max(len(self.input_pins.values()), len(self.output_pins.values()))+70

    def add_input_pin(self, name, type):
        pin = Pin(self, type=type, valuename=name)
        if len(self.input_pins) > 0:
            pin.defRelPos(pin.getRelPos()[0], [x for x in self.input_pins.values()][-1].getRelPos()[
                1] + CONST_SPACE_BETWEEN_PINS + CONST_PIN_HEIGHT)
        self.ch.append(pin)
        self.input_pins.update({name: pin})
        self.scene().addItem(pin)
        self.update()
        self.adjustBlockSize()

    def add_output_pins(self, name, type):
        pin = Pin(self, type=type, valuename=name)
        self.ch.append(pin)
        self.output_pins.update({name: pin})
        self.scene().addItem(pin)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        self.moveBy(event.pos().x() - event.lastPos().x(), event.pos().y() - event.lastPos().y())
        print(event.pos().toTuple(), event.lastPos().toTuple(), QPointF(event.pos() - event.lastPos()).toTuple())
        for child in self.ch:
            child.moveBy(event.pos().x() - event.lastPos().x(), event.pos().y() - event.lastPos().y())


app = QApplication([])

scene = QGraphicsScene()
custom_item = Node(scene, "a", NodeType.OPERATOR)

view = QGraphicsView(scene)
view.show()

app.exec()
