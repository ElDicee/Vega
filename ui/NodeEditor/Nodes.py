import random
from inspect import signature

import PySide6
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QRectF, QPointF, QPoint
from PySide6.QtGui import QColor, QPainterPath, QBrush, QLinearGradient, QPen, QFont, QFontMetrics, QPolygonF, QPainter
from PySide6.QtWidgets import QGraphicsItem, QWidget, QGraphicsPathItem, QGraphicsSceneMouseEvent, \
    QGraphicsSceneDragDropEvent, QLineEdit, QGraphicsProxyWidget, QTextEdit, QGraphicsRectItem, QGraphicsTextItem, \
    QPushButton, QCheckBox


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

    def get_opposite_pin(self, pin):
        return self.start_pin if pin != self.start_pin else self.end_pin

    def nodes(self):
        return self.start_pin.node(), self.end_pin.node()

    def update_start_end_pos(self):
        if self.start_pin and not self.start_pin.output:
            self.end_pin, self.start_pin = self.start_pin, self.end_pin
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
        y = round(self.radius * 2 - self.pin_text_height / 2)
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
        return self.output != pin.output and (self.datatype == pin.datatype or not self.datatype or not pin.datatype)

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

        if not self.exec or (self.exec and (str(self.name).lower() != "out" and str(self.name).lower() != "in")):
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(Qt.GlobalColor.white)
            painter.drawPath(self.text_path)

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged and self.is_connected():
            for x in self.connections:
                x.update_start_end_pos()
                x.updatePath()
        return value


class LineEdit(QGraphicsProxyWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        btn = QPushButton("Hello, World!")
        btn.clicked.connect(lambda: print("Hello World!"))
        self.setWidget(btn)
        self.focusItem()

    def mousePressEvent(self, event):
        self.widget().setFocus()

    def boundingRect(self):
        return self.rect()


class Node(QGraphicsItem):
    def __init__(self, name, section, vega, additional_widget=None, **kwargs):
        super().__init__()

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        self.title_text = name
        self.title_color = QColor(123, 33, 177)
        if kwargs.get("node_color"):
            self.title_color = QColor(kwargs.get("node_color")[0], kwargs.get("node_color")[1],
                                      kwargs.get("node_color")[2])
        self.size = QRectF()
        self.function = None
        self.execution_policy = None
        self.allowMove = False
        self.use_display = False
        self.vega = vega

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
        self.integration = None
        self.computed_data = None
        self.event = False
        self.event_itg = None
        self.event_name = None
        self.is_exec = False
        self.id_name = self.title_text

        self.output_data = {}

        self.node_color = QColor(20, 20, 20, 200)
        self.title_path = QPainterPath()
        self.type_path = QPainterPath()
        self.misc_path = QPainterPath()

        self.horizontal_margin = 15
        self.vertical_margin = 2

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

        inp = [pin for pin in self.pins if not pin.output]
        outp = [pin for pin in self.pins if pin.output]

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
        if title_type_dim["w"] > total_width: total_width = title_type_dim["w"]

        total_height = bg_height + self.widget.size().height()

        pin1_dim = {}
        pin2_dim = {}

        larg = inp if len(inp) > len(outp) else outp

        for j in range(len(larg)):
            in_p = inp[j].name if len(inp) >= j + 1 else ""
            out_p = outp[j].name if len(outp) >= j + 1 else ""

            pin1_dim.update(
                {"w": QFontMetrics(pin_font).horizontalAdvance(in_p),
                 "h": QFontMetrics(pin_font).height()})

            pin2_dim.update(
                {"w": QFontMetrics(pin_font).horizontalAdvance(out_p),
                 "h": QFontMetrics(pin_font).height()})

            total_width = max(total_width, pin1_dim["w"] + pin2_dim["w"])

            # if pin.exec and not exec_height_added or not pin.exec:
            # total_height += pin_dim["h"] + self.vertical_margin

        total_height += max(len(inp), len(outp)) * (pin1_dim["h"] + self.vertical_margin) + 5
        if isinstance(self, I_Node):
            total_height += self.proxy.size().height() + 5

        total_width += self.horizontal_margin * 3

        self.size = QRectF(-total_width / 2, -total_height / 2, total_width, total_height)
        self.path.addRoundedRect(-total_width / 2, -total_height / 2, total_width, total_height, 5, 5)

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

        # y = bg_height - total_height / 2 - 10 + pin_dim["h"]
        # execpos = None
        # for pin in self.pins:
        #     if pin.exec:
        #         if not execpos:
        #             execpos = bg_height - total_height / 2 - 10 + pin_dim["h"]
        #         pin.setPos(total_width / 2 - 10, y) if pin.output else pin.setPos(-total_width / 2 + 10, y)
        #         y += pin_dim["h"]
        #     else:
        #         y += pin_dim["h"]
        #         if pin.output:
        #             pin.setPos(total_width / 2 - 10, y)
        #         else:
        #             pin.setPos(-total_width / 2 + 10, y)

        y = -total_height / 2 + bg_height + pin1_dim["h"]
        for pin in inp:
            pin.setPos(-total_width / 2 + 10, y)
            y += pin1_dim["h"]

        y = -total_height / 2 + bg_height + pin1_dim["h"]
        for pin in outp:
            pin.setPos(total_width / 2 - 10, y)
            y += pin1_dim["h"]

        self.width = total_width
        self.height = total_height
        self.larg = larg
        self.widget.move(-self.widget.size().width() / 2, total_height / 2 - self.widget.size().height() + 5)

    def delete(self):
        # for connection in [pin.connection for pin in self.pins if pin.is_connected()]:
        for pin in self.pins:
            if pin.is_connected():
                for connection in pin.connections:
                    connection.delete()
        self.scene().removeItem(self)
        if self.event:
            self.vega.event_nodes.get(self.event_itg).pop(self.event_name)

    def get_pin(self, name):
        for pin in self.pins:
            print(pin.name)
            if pin.name == name:
                return pin

    def get_exec_pin(self, name):
        for pin in self.pins:
            if pin.exec and pin.name == name:
                return pin

    def add_pin(self, name, exec=False, output=False, datatype=object):
        self.pins.append(Pin(self, self.scene(), valuename=name, execution=exec, output=output, datatype=datatype))
        if exec: self.is_exec = True

    def add_widget(self):
        self.vega_widget = LineEdit(parent=self)

    def select_connections(self, value):
        for pin in self.pins:
            if pin.is_connected():
                for con in pin.connections:
                    con.highlight = value
                    con.updatePath()

    def get_input_pins(self):
        pins = []
        for p in self.pins:
            if not p.output and not p.exec:
                pins.append(p)
        return pins if len(pins) > 0 else None

    def get_exec_pins(self):
        p = []
        for pin in self.pins:
            if pin.exec: p.append(pin)
        return p

    def get_output_pins(self):
        pins = []
        for p in self.pins:
            if p.output and not p.exec:
                pins.append(p)
        return pins if len(pins) > 0 else None

    def get_next_exec_pin(self):
        pin = None
        for p in self.pins:
            if p.exec and p.output:
                if len(p.connections) > 0:
                    pin = p.connections[0].get_opposite_pin(p)
                break
        return pin

    def execute(self):
        # CHECK NODE INPUTS AND CALCULATE NEEDED DATA
        # PERFORM ACTION
        # NEXT NODE

        needed_data = {}
        if not self.event:
            inp = self.get_input_pins()
            if inp:
                for i in inp:
                    print(i.name, i.connections)
                    if len(i.connections) > 0:
                        print(i)
                        opp = i.connections[0].get_opposite_pin(i)
                        print(opp.name)
                        node = opp.node
                        if node.is_exec:
                            needed_data.update({opp.name: node.output_data.get(opp.name)})
                        else:
                            node.execute()
                            if node.integration == "Vega":
                                needed_data.update({node.uuid.__str__: node.output_data.get(node.uuid.__str__)})
                            else:
                                needed_data.update({opp.name: node.output_data.get(opp.name)})
            print(f"Vals: {needed_data.values()}")
            res = self.function(*needed_data.values()) if self.function else None
            outp = self.get_output_pins()
            if outp:
                if self.is_exec:
                    if res is not None:
                        if isinstance(res, dict):
                            for i, o in enumerate(outp):
                                self.output_data.update({o.name: res[i]})
                        else:
                            self.output_data.update({outp[0].name: res})
                else:
                    self.output_data.update(
                        {o.name if self.integration != "Vega" else self.uuid.__str__: res for o in outp})
        if self.is_exec:
            if not self.execution_policy:
                flow_pin = self.get_next_exec_pin()
                if flow_pin: flow_pin.node.execute()
            else:
                self.execution_policy(self.run_policy,
                                      *list(needed_data.values())[-len(get_func_params(self.execution_policy)):])

    def run_policy(self, pin_id, elements=None):
        if elements is None: elements = {}
        self.output_data.update(elements)
        ex_pin = self.get_exec_pin(pin_id)
        if len(ex_pin.connections) > 0: ex_pin.connections[0].get_opposite_pin(ex_pin).node.execute()


def get_func_params(func):
    if func:
        sign = signature(func)
        return [str(x) for x in sign.parameters.values()]


class I_Node(Node):

    def __init__(self, name, section, vega, data_type, additional_widget=None, **kwargs):
        super().__init__(name, section, vega, additional_widget=additional_widget, **kwargs)
        self.sc = None
        self.data_type = data_type
        self.element = None

        if self.data_type == str:
            self.element = QLineEdit()
            self.element.setStyleSheet(u"""color: rgb(255, 255, 255);
border-top-left-radius: 10px;
border-top-right-radius: 10px;
border-bottom: 3px solid qlineargradient(spread:pad, x1:0.0397727, y1:0.528, x2:1, y2:0.596591, stop:0 rgba(68, 228, 227, 255), stop:0.517045 rgba(104, 57, 255, 227), stop:0.9375 rgba(221, 39, 255, 255));""")
            self.element.setPlaceholderText("Write a text...")
            self.function = lambda: str(self.element.text())
        elif self.data_type == int:
            self.element = IntLineEdit()
            self.element.setStyleSheet(u"""color: rgb(255, 255, 255);
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom: 3px solid qlineargradient(spread:pad, x1:0.0397727, y1:0.528, x2:1, y2:0.596591, stop:0 rgba(68, 228, 227, 255), stop:0.517045 rgba(104, 57, 255, 227), stop:0.9375 rgba(221, 39, 255, 255));""")
            self.function = lambda: int(self.element.text())
            self.element.setText("0")
        elif self.data_type == float:
            self.element = FloatLineEdit()
            self.element.setStyleSheet(u"""color: rgb(255, 255, 255);
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom: 3px solid qlineargradient(spread:pad, x1:0.0397727, y1:0.528, x2:1, y2:0.596591, stop:0 rgba(68, 228, 227, 255), stop:0.517045 rgba(104, 57, 255, 227), stop:0.9375 rgba(221, 39, 255, 255));""")
            self.function = lambda: float(self.element.text())
            self.element.setText("0.0")
        elif self.data_type == bool:
            self.element = QCheckBox()
            self.function = lambda: bool(self.element.isChecked())

    def build(self):
        self.init_widget()
        super().build()
        self.proxy.setPos(-self.widget.size().width() / 2, self.larg[-1].pos().y() + 5)

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.element)
        self.widget.setLayout(layout)
        self.proxy = QtWidgets.QGraphicsProxyWidget()
        self.proxy.setWidget(self.widget)
        self.proxy.setParentItem(self)


class FloatLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent):
        if str(event.text()).isnumeric() or (
                not "." in self.text() and event.text() == ".") or event.key() == Qt.Key.Key_Backspace:
            super().keyPressEvent(event)


class IntLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent):
        if str(event.text()).isnumeric() or event.key() == Qt.Key.Key_Backspace:
            super().keyPressEvent(event)
