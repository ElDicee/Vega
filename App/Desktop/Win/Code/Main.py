import importlib.util

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
import sys
import os
import socket
import ui.ok_ui as ui_m
from random import randint
import json


class Integration:
    def __init__(self, path, vega):
        self.name = None
        self.enabled = True
        self.display = None
        self.methods = {}
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
                    print(i)
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
            print("loaded", m.name)
        self.display = veg.display


class Vega:
    instance = None

    def __init__(self):
        self.main_frame = None
        self.app = QApplication(sys.argv)
        self.integrations = {}
        self.itg_folder_path = f"{os.path.abspath(os.path.dirname(__file__))}\integrations"
        self.connection_portal = ConnectionPortal(7778)
        self.load_bar = ui_m.LoadBar()
        self.instance = self
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.connect(self.connection_portal.receive_data)

    def load_integrations(self):
        self.load_bar.show()
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
        self.load_bar.destroy(True)

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
        self.instance = self
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
            for node in EventManager.get_instance().event_nodes:
                if node.name == data.values()[0].get("event"):
                    pass

    def define_port(self):
        with open(f"{os.getenv('APPDATA')}\Vega\ports.veg", "w") as file:
            file.write(f"Port: {str(self.port)}")
            file.close()

    def close_connection(self):
        self.socket.close()

    def change_data_buffer(self, buf: int):
        self.buffer = max(buf, 1024)


if __name__ == "__main__":
    vega = Vega()
    vega.load_integrations()
    vega.start_main_ui()
