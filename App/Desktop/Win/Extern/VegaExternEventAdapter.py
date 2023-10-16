import socket
import threading
import json


class VegaEvent:
    def __init__(self, name, description="No information available.", vega_exec=False):
        self.name = name
        self.desc = description
        self.func = None
        self.params = {}
        self.vega_exec = vega_exec #si s'ha de realitzar a vega o al programa extern

    def set_function(self, func):
        self.func = func

    def add_param(self, name, typ):  # NAME, INT/STR ETC
        self.params.update({name, typ})

    def run(self, **kwargs):
        self.func(**kwargs)


class ServerWorker:
    def __init__(self, parent, conn: socket.socket, addr):
        self.parent = parent
        self.addr = addr
        self.connection: socket.socket = conn
        self.is_alive = True
        threading.Thread(target=self.receive).start()

    def receive(self):
        while self.is_alive:
            data = self.connection.recv(self.parent.buffer_size).decode()
            if data == "close_socket":
                self.is_alive = False
                self.parent.connections.pop(self.addr)
            else:
                self.parse_event(data)

    def parse_event(self, str):
        try:
            content = json.loads(str)
            name = content.get("name")
            data = content.get("data")
            event = self.parent.event_list.get(name)
            if not event.vega_exec:
                event.run(**data)  # empaquetar dict
        except:
            pass


class VegaClient_Server(socket.socket):
    def __init__(self, id, ip, port):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.id = id
        self.ip = ip
        self.port = port
        self.buffer_size = 1024
        self.connections = {}
        self.is_closing = False
        self.event_list = {}

    def add_event_info(self, event: VegaEvent):
        self.event_list.update({event.name, event})

    def try_connection(self):
        try:
            self.bind((self.ip, self.port))
            self.listen(-1)
        except:
            raise f"Could not connect to {self.ip}:{self.port}"

    def start_receiving(self):
        while not self.is_closing:
            conn, addr = self.accept()
            conn.sendall(json.dumps({"ID": self.id,
                                     "events": {name:{"desc": e.desc, "vega_exec":e.vega_bound, "params": e.params} for name, e in self.event_list.items()}
                                     }).encode())
            s = ServerWorker(self, conn, addr)
            self.connections.update({addr, s})