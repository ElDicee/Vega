from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QStackedWidget, QVBoxLayout, QWidget

app = QApplication([])

# Crear los widgets que se mostrarán en la pila
widget1 = QLabel("Widget 1")
widget2 = QPushButton("Widget 2")
widget3 = QLabel("Widget 3")

# Crear el QStackedWidget y agregar los widgets a la pila
stackedWidget = QStackedWidget()
stackedWidget.addWidget(widget1)
stackedWidget.addWidget(widget2)
stackedWidget.addWidget(widget3)

# Crear un layout vertical y agregar el QStackedWidget a él
layout = QVBoxLayout()
layout.addWidget(stackedWidget)

# Crear un widget principal y establecer el layout en él
mainWidget = QWidget()
mainWidget.setLayout(layout)
mainWidget.show()

# Cambiar el widget visible en la pila
stackedWidget.setCurrentIndex(1)

app.exec()