import importlib.util

from PySide6.QtCore import QTimer, QThread, Signal
from PySide6.QtWidgets import QApplication
import sys
import os
import socket
import ui.ok_ui as ui_m
from random import randint
import json


class Integration:
    def __init__(self, name, path, vega):
        self.name = name
        self.enabled = True
        self.display = None
        self.methods = {}
        self.events = []
        self.load_class(path)
        self.vega = vega

    def method_loader(self, e):
        inp = {}
        kw, args = False, False
        for i in e.inputs:
            if i.startswith("**"):
                kw = True
            elif i.startswith("*"):
                args = True
            else:
                if ":" in i:
                    inp.update({i.split(":")[0]: self.str_to_type(i.split(":")[1])})
                else:
                    inp.update({i: object})
            self.methods.update({e.name: {"func": e.func, "inputs": inp, "extend": [kw, args], "node": e.node_type,
                                          "outs": e.output_types, "formal_name": e.formal_name}})

    def str_to_type(self, name):
        name = name.lstrip().rstrip()
        if name.lower() == "int":
            return int
        if name.lower() == "str":
            return str
        if name.lower() == "float":
            return float
        if name.lower() == "object":
            return object

    def load_class(self, path):
        spec = importlib.util.spec_from_file_location(self.name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        veg = mod.vega_main()
        self.name = veg.name
        methods = veg.methods
        veg.vega_main_software_class = self
        for m in methods:
            self.method_loader(m)
            print("Loaded: ", m.name)
        for e in veg.events:
            self.events.append(e.name)
        self.display = veg.display


def install_needed_files(files: dict): #https://www.pythoncheatsheet.org/cheatsheet/file-directory-path    https://stackoverflow.com/questions/13184414/how-can-i-get-the-path-to-the-appdata-directory-in-python
    roaming = os.getenv("APPDATA")
    vega_folder = ".vega"
    fold_path = os.path.join(roaming, vega_folder)
    if not vega_folder in os.listdir(roaming):
        os.mkdir(fold_path)
        for f, d in files:
            with open(os.path.join(fold_path, f"{f}.veg"), "w") as file:
                file.write(d)
                file.close()
    else:
        with os.scandir(fold_path) as scan:
            for entry in scan:
                if entry.is_file() and entry.name[:-4] in files.keys():
                    files.pop(entry.name[:-4])
        for remaining in files:
            with open(f"{os.path.join(fold_path, remaining)}.veg", "w") as scan:
                scan.write(files.get(remaining))
                scan.close()


class Vega:
    instance = None

    def __init__(self):

        install_needed_files({"ports": "Ports: 7773"})

        self.main_frame = None
        self.app = QApplication(sys.argv)
        self.integrations = {}
        self.event_manager = EventManager()
        self.itg_folder_path = f"{os.path.abspath(os.path.dirname(__file__))}\integrations"
        self.connection_portal = ConnectionPortal(7778)
        self.connection_thread = ConnectionThread(self.connection_portal)
        self.connection_thread.start()

        # self.load_bar = ui_m.LoadBar()
        self.instance = self

    def load_integrations(self):
        # self.load_bar.show()
        self.integrations.clear()
        with os.scandir(self.itg_folder_path) as scan:
            for entry in scan:
                if entry.is_dir():
                    with os.scandir(os.path.abspath(entry)) as foldscan:
                        for file in foldscan:
                            if file.name == "main.py":
                                itg = Integration(entry.name, f"{os.path.abspath(entry)}\main.py", self)
                                self.integrations.update({itg.name: itg})
                                break
        # self.load_bar.destroy(True)

    def add_loading(self):
        pass

    @classmethod
    def get_instance(cls):
        return cls.instance

    def start_main_ui(self):
        self.main_frame = ui_m.MainFrame(self, show=True)
        sys.exit(self.app.exec())


class EventManager:

    instance = None

    def __init__(self):
        setattr(EventManager, "instance", self)
        self.event_queue = []
        self.event_nodes = []

    @classmethod
    def get_instance(cls):
        return cls.instance


class ConnectionPortal:
    def __init__(self, port):
        print("creating socket")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        try:
            print("starting connection")
            self.start_connection()
        except OSError:
            self.port = randint(49152, 65535)
            self.start_connection()
        self.buffer = 1024
        self.command_query = []

    def start_connection(self):
        self.socket.bind(("127.0.0.1", self.port))
        self.define_port()
        self.socket.listen(1)

    def receive_data(self):
        client, addr = self.socket.accept()
        data = json.loads(client.recv(self.buffer).decode())
        if data:
            print(data)
            for node in EventManager.get_instance().event_nodes:
                if node.name == data.values()[0].get("event"):
                    pass

    def define_port(self):
        with open(os.path.join(os.getenv("APPDATA"), ".vega", "ports.veg"), "w") as file:
            file.write(f"Port: {str(self.port)}")
            file.close()

    def close_connection(self):
        self.socket.close()

    def change_data_buffer(self, buf: int):
        self.buffer = max(buf, 1024)


class ConnectionThread(QThread): #https://doc.qt.io/qtforpython-6/PySide6/QtCore/QThread.html

    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.connection.receive_data)
        self.timer.start()


if __name__ == "__main__":
    vega = Vega()
    vega.load_integrations()
    vega.start_main_ui()
