from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QColor, QPainterPath, QBrush, QLinearGradient, QPen, QFont, QFontMetrics, QPolygonF
from PySide6.QtWidgets import QGraphicsItem, QWidget, QGraphicsPathItem, QGraphicsSceneMouseEvent, \
    QGraphicsSceneDragDropEvent
from enum import Enum


def color_from_type(type):
    if type == int:
        return QColor(56, 200, 232)
    elif type == float:
        return QColor(25, 189, 25)
    elif type == str:
        return QColor(186, 43, 35)
    elif type == object:
        return QColor(227, 188, 70)
    else:
        return QColor(209, 204, 219)


class Connection(QGraphicsPathItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setFlag(QGraphicsPathItem.GraphicsItemFlag.ItemIsSelectable)
        self.setPen(QPen(QColor(200, 200, 200), 2))
        self.setBrush(Qt.BrushStyle.NoBrush)
        self.setZValue(-1)

        self.start_pos = QPointF()
        self.end_pos = QPointF()
        self.start_pin = None
        self.end_pin = None

        self.highlight = False

    def updatePath(self):
        path = QPainterPath()
        path.moveTo(self.start_pos)

        dist_x = self.end_pos.x() - self.start_pos.x()
        dist_y = self.end_pos.y() - self.start_pos.y()

        ctr1 = QPointF(self.start_pos.x() + dist_x * 0.5, self.start_pos.y())
        ctr2 = QPointF(self.start_pos.x() + dist_x * 0.5, self.start_pos.y() + dist_y)
        path.cubicTo(ctr1, ctr2, self.end_pos)
        self.setPath(path)

    def paint(self, painter, option=None, widget=None):

        thickness = 0
        color = QColor(0, 128, 255)
        if self.start_pin:
            if self.start_pin.exec:
                thickness = 3
                color = QColor(255, 255, 255)

        if self.isSelected() or self.highlight:
            painter.setPen(QPen(color.lighter(), thickness + 2))
        else:
            painter.setPen(QPen(color, thickness))
        painter.drawPath(self.path())

    def delete(self):
        self.scene().removeItem(self)
        if self.start_pin:
            self.start_pin.connections.remove(self)
            self.start_pin = None
        if self.end_pin:
            self.end_pin.connections.remove(self)
            self.end_pin = None

    def set_start_pin(self, pin):
        self.start_pin = pin
        self.start_pos = pin.scenePos()
        pin.connections.append(self)

    def set_end_pin(self, pin):
        self.end_pin = pin
        self.end_pos = pin.scenePos()
        pin.connections.append(self)

    def nodes(self):
        return self.start_pin.node(), self.end_pin.node()

    def update_start_end_pos(self):
        if self.start_pin and not self.start_pin.output:
            self.end_pin, self.start_pin = self.start_pos, self.end_pin
        if self.start_pin:
            self.start_pos = self.start_pin.scenePos()
        if self.end_pin:
            self.end_pos = self.end_pin.scenePos()
        self.updatePath()


class Pin(QGraphicsPathItem):
    def __init__(self, parent, scene, valuename, datatype=object, execution=False, output=False):
        super().__init__(parent)

        self.radius = 5
        self.margin = 2
        self.exec = execution
        self.output = output
        self.node = parent
        self.name = valuename
        self.connections = []
        self.datatype = datatype
        print(self.datatype)
        self.sc = scene

        path = QPainterPath()
        path.addEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)
        self.setPath(path)

        self.setFlag(QGraphicsPathItem.GraphicsItemFlag.ItemSendsScenePositionChanges)
        self.text_path = QPainterPath()

        self.font = QFont()
        self.font_metrics = QFontMetrics(self.font)
        self.pin_text_height = self.font_metrics.height()

        if execution:
            path.clear()
            points = []
            points.append(QPointF(-6, -7))
            points.append(QPointF(-6, 7))
            points.append(QPointF(-2, 7))
            points.append(QPointF(6, 0))
            points.append(QPointF(-2, -7))
            points.append(QPointF(-6, -7))
            path.addPolygon(QPolygonF(points))
            self.setPath(path)

        valuename = valuename.replace("_", " ").title()
        self.pin_text_width = self.font_metrics.horizontalAdvance(valuename)

        if output:
            x = -self.radius - self.margin - self.pin_text_width
        else:
            x = self.radius + self.margin
        y = round(self.radius - self.pin_text_height / 2)
        self.text_path.addText(x, y, self.font, valuename)

    def is_connected(self):
        return len(self.connections) > 0

    # def clear_connections(self):
    #     if self.is_connected():
    #         for c in self.connections:
    #             c.delete()

    def can_connect_to(self, pin):
        if not pin:
            return False
        if pin.node == self.node:
            return False
        if pin.exec != self.exec:
            return False
        return self.output != pin.output and self.datatype == pin.datatype

    def paint(self, painter, option: None, widget=None):
        if self.exec:
            painter.setPen(Qt.GlobalColor.white)
        else:
            painter.setPen(color_from_type(self.datatype))

        if self.is_connected():
            if self.exec:
                painter.setBrush(Qt.GlobalColor.white)
            else:
                painter.setPen(color_from_type(self.datatype))
        else:
            painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(self.path())

        if not self.exec:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(Qt.GlobalColor.white)
            painter.drawPath(self.text_path)

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged and self.is_connected():
            for x in self.connections:
                x.update_start_end_pos()
                x.updatePath()
        return value


class Node(QGraphicsItem):
    def __init__(self, name, section, additional_widget=None):
        super().__init__()

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        self.title_text = name
        self.title_color = QColor(123, 33, 177)
        self.size = QRectF()
        self.function = None
        self.allowMove = False

        if not additional_widget:
            self.widget = QWidget()
            self.widget.resize(0, 0)
        else:
            self.widget = additional_widget

        self.type_text = section
        self.width = 20
        self.height = 20
        self.pins = []
        self.uuid = None

        self.node_color = QColor(20, 20, 20, 200)
        self.title_path = QPainterPath()
        self.type_path = QPainterPath()
        self.misc_path = QPainterPath()

        self.horizontal_margin = 15
        self.vertical_margin = 15

    def boundingRect(self):
        return self.size

    def set_function(self, func):
        self.function = func

    def set_color(self, title=(123, 33, 177), bg=(20, 20, 20, 200)):
        self.title_color = QColor(title[0], title[1], title[2])
        self.node_color = QColor(bg[0], bg[1], bg[2])

    def paint(self, painter, option=None, widget=None):
        painter.setPen(self.node_color.lighter())
        painter.setBrush(self.node_color)
        painter.drawPath(self.path)

        gradient = QLinearGradient()
        gradient.setStart(0, -90)
        gradient.setFinalStop(0, 0)
        gradient.setColorAt(0, self.title_color)
        gradient.setColorAt(1, self.title_color.darker())

        painter.setBrush(QBrush(gradient))
        painter.setPen(self.title_color)
        painter.drawPath(self.title_bg_path.simplified())

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(Qt.GlobalColor.white)

        painter.drawPath(self.title_path)
        painter.drawPath(self.type_path)
        painter.drawPath(self.misc_path)

        if self.isSelected():
            painter.setPen(QPen(self.title_color.lighter(), 2))
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawPath(self.path)

    def build(self):

        self.widget.setStyleSheet("background-color: " + self.node_color.name() + ";")
        self.title_path = QPainterPath()
        self.type_path = QPainterPath()
        self.misc_path = QPainterPath()

        bg_height = 35

        total_width = self.widget.size().width()
        self.path = QPainterPath()
        title_font = QFont("Lucida Sans Unicode", pointSize=12)
        title_type_font = QFont("Lucida Sans Unicode", pointSize=8)
        pin_font = QFont("Lucida Sans Unicode")

        title_dim = {
            "w": QFontMetrics(title_font).horizontalAdvance(f"{self.title_text}"),
            "h": QFontMetrics(title_font).height()
        }

        title_type_dim = {
            "w": QFontMetrics(title_type_font).horizontalAdvance(f"{self.type_text}"),
            "h": QFontMetrics(title_type_font).height()
        }

        if title_dim["w"] > total_width: total_width = title_dim["w"]
        if title_type_dim["w"] > total_width: total_width = title_type_font["w"]

        total_height = bg_height + self.widget.size().height()

        exec_height_added = False
        pin_dim = {}
        for pin in self.pins:
            pin_dim.update(
                {"w": QFontMetrics(pin_font).horizontalAdvance(pin.name),
                 "h": QFontMetrics(pin_font).height()})

            total_width = max(total_width, pin_dim["w"])

            if pin.exec and not exec_height_added or not pin.exec:
                total_height += pin_dim["h"]
                exec_height_added = True

        total_width += self.horizontal_margin

        self.size = QRectF(-total_width / 2, -total_height / 2, total_width, total_height)
        self.path.addRoundedRect(-total_width / 2, -total_height / 2, total_width, total_height + 10, 5, 5)

        self.title_bg_path = QPainterPath()  # The title background path
        self.title_bg_path.setFillRule(Qt.WindingFill)
        self.title_bg_path.addRoundedRect(-total_width / 2, -total_height / 2, total_width, bg_height, 5, 5)
        self.title_bg_path.addRect(-total_width / 2, -total_height / 2 + bg_height - 10, 10, 10)  # bottom left corner
        self.title_bg_path.addRect(total_width / 2 - 10, -total_height / 2 + bg_height - 10, 10,
                                   10)  # bottom right corner

        self.title_path.addText(
            -total_width / 2 + 5,
            (-total_height / 2) + title_dim["h"] / 2 + 5,
            title_font,
            self.title_text,
        )

        # Draw the type
        self.type_path.addText(
            -total_width / 2 + 5,
            (-total_height / 2) + title_dim["h"] + 5,
            title_type_font,
            f"{self.type_text}",
        )

        y = bg_height - total_height / 2 - 10 + pin_dim["h"]
        execpos = None
        for pin in self.pins:
            if pin.exec:
                if not execpos:
                    execpos = bg_height - total_height / 2 - 10 + pin_dim["h"]
                pin.setPos(total_width / 2 - 10, execpos) if pin.output else pin.setPos(-total_width / 2 + 10, execpos)
            else:
                y += pin_dim["h"]
                if pin.output:
                    pin.setPos(total_width / 2 - 10, y)
                else:
                    pin.setPos(-total_width / 2 + 10, y)
        self.width = total_width
        self.height = total_height
        self.widget.move(-self.widget.size().width() / 2, total_height / 2 - self.widget.size().height() + 5)

    def delete(self):
        #for connection in [pin.connection for pin in self.pins if pin.is_connected()]:
        for connection in [(con for con in pin.connections) for pin in self.pins if pin.is_connected()]:
            connection.delete()
        self.scene().removeItem(self)

    def get_pin(self, name):
        for pin in self.pins:
            if pin.name == name:
                return pin

    def add_pin(self, name, exec=False, output=False, datatype=object):
        self.pins.append(Pin(self, self.scene(), valuename=name, execution=exec, output=output, datatype=datatype))

    def select_connections(self, value):
        for pin in self.pins:
            if pin.is_connected():
                for con in pin.connections:
                    con.highlight = value
                    con.updatePath()
