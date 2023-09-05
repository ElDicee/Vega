import random
from contextlib import suppress

from PySide6.QtCore import QObject, QPointF, QRectF, QSizeF, Qt, QEvent
from PySide6.QtWidgets import QWidgetItem

from App.Desktop.Win.Code.ui.NodeEditor.Nodes import Pin, Connection, Node


class NodeLogic(QObject):
    """
    The main class of the node editor. This class handles the logic for creating, connecting, and deleting
    nodes and connections.
        :ivar connection: A Connection object representing the current connection being created.
    :vartype connection: Connection
    :ivar port: A Pin object representing the current port being clicked for a new connection.
    :vartype port: Pin
    :ivar scene: The QGraphicsScene on which the nodes and connections are drawn.
    :vartype scene: QGraphicsScene
    :ivar _last_selected: The last Node object that was selected.
    :vartype _last_selected: Node
    """

    def __init__(self, parent):
        """
        Constructor for NodeEditor.

        :param parent: The parent widget.
        :type parent: QWidget
        """

        super().__init__(parent)
        self.connection = None
        self.port = None
        self.scene = None
        self._last_selected = None

    def install(self, scene):
        """
        Installs the NodeEditor into a QGraphicsScene.

        :param scene: The QGraphicsScene to install the NodeEditor into.
        :type scene: QGraphicsScene
        """

        self.scene = scene
        self.scene.installEventFilter(self)

    def item_at(self, position):
        """
        Returns the QGraphicsItem at the given position.

        :param position: The position to check for a QGraphicsItem.
        :type position: QPoint
        :return: The QGraphicsItem at the position, or None if no item is found.
        :rtype: QGraphicsItem
        """

        items = self.scene.items(QRectF(position - QPointF(1, 1), QSizeF(3, 3)))
        return items[0] if items else None

    def eventFilter(self, watched, event):
        """
        Filters events from the QGraphicsScene.

        :param watched: The object that is watched.
        :type watched: QObject
        :param event: The event that is being filtered.
        :type event: QEvent
        :return: True if the event was filtered, False otherwise.
        :rtype: bool
        """
        if type(event) == QWidgetItem:
            return False

        if event.type() == QEvent.GraphicsSceneMousePress:
            if event.button() == Qt.LeftButton:
                item = self.item_at(event.scenePos())

                if isinstance(item, Pin):
                    self.connection = Connection(None)
                    self.scene.addItem(self.connection)
                    self.port = item
                    self.connection.start_pos = item.scenePos()
                    self.connection.end_pos = event.scenePos()
                    self.connection.updatePath()
                    return True

                if isinstance(item, Connection):
                    self.connection = Connection(None)
                    self.connection.start_pos = item.start_pos
                    self.scene.addItem(self.connection)
                    self.port = item.start_pin
                    self.connection.end_pos = event.scenePos()
                    self.connection.update_start_end_pos()  # to fix the offset
                    return True

                if self._last_selected:
                    # If we clear the scene, we loose the last selection
                    with suppress(RuntimeError):
                        self._last_selected.select_connections(False)

                if isinstance(item, Node):
                    item.select_connections(True)
                    self._last_selected = item
                else:
                    self._last_selected = None

        elif event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Delete:
                for item in self.scene.selectedItems():
                    if isinstance(item, (Connection, Node)):
                        item.delete()

                return True

        elif event.type() == QEvent.GraphicsSceneMouseMove:
            if self.connection:
                print(random.randint(1, 1000))
                self.connection.end_pos = event.scenePos()
                self.connection.updatePath()
                return True

        elif event.type() == QEvent.GraphicsSceneMouseRelease:
            if self.connection and event.button() == Qt.LeftButton:
                item = self.item_at(event.scenePos())

                # connecting a port
                if isinstance(item, Pin):
                    if self.port.can_connect_to(item):
                        # print("Making connection")

                        # delete existing connection on the new port
                        if item.connection:
                            item.connection.delete()

                        # delete existing connection to the original port
                        self.port.clear_connection()
                        item.clear_connection()

                        self.connection.set_start_pin(self.port)
                        self.connection.set_end_pin(item)
                        self.connection.update_start_end_pos()
                    else:
                        # print("Deleting connection")
                        self.connection.delete()

                    self.connection = None

                if self.connection:
                    self.connection.delete()
                self.connection = None
                self.port = None
                return True

        return super().eventFilter(watched, event)