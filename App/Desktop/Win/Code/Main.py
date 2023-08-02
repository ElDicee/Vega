import importlib.util

from PySide6.QtWidgets import QApplication
import sys
import os
import socket
import ok_ui as ui_m
from random import randint


class Integration:
    def __init__(self, name, path):
        self.name = name
        self.enabled = True
        self.methods = {}
        self.load_class(path)

    def method_loader(self, e):
        inp = {}
        kw, args = False
        for i in e[2]:
            i = str(i)
            if i.startswith("**"):
                kw = True
            elif i.startswith("*"):
                args = True
            else:
                if ":" in i:
                    inp.update({i.split(":")[0]: i.split(":")[1]})
                else:
                    inp.update({i: "object"})
            self.methods.update({e[0]: {"func": e[1], "inputs": inp, "extend": [kw, args]}})

    def load_class(self, path):
        spec = importlib.util.spec_from_file_location(self.name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        methods = mod.vega_main().methods
        for m in methods:
            self.method_loader(m)
            print("loaded", m[0])
        del sys.modules[spec.name]


class Vega:
    def __init__(self):
        self.main_frame = None
        self.app = QApplication(sys.argv)
        self.integrations = {}
        self.itg_folder_path = f"{os.path.abspath(os.path.dirname(__file__))}\integrations"
        self.connection_portal = ConnectionPortal(6969)

    def load_integrations(self):
        self.integrations.clear()
        with os.scandir(self.itg_folder_path) as scan:
            for entry in scan:
                if not entry.is_file():
                    with os.scandir(os.path.abspath(entry)) as foldscan:
                        for file in foldscan:
                            if file.name == "main.py":
                                itg = Integration(entry.name, f"{os.path.abspath(entry)}\main.py")
                                self.integrations.update({itg.name: itg})
                                break

    def get_integrations(self):
        return self.integrations

    def start_main_ui(self):
        self.main_frame = ui_m.MainFrame(self)
        self.main_frame.show()
        sys.exit(self.app.exec())


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
        self.socket.listen(1)

    def receive_data(self):
        client, addr = self.socket.accept()
        return client.recv(self.buffer)

    def close_connection(self):
        self.socket.close()

    def change_data_buffer(self, buf: int):
        self.buffer = max(buf, 1024)


if __name__ == "__main__":
    vega = Vega()
    vega.start_main_ui()
    vega.load_integrations()