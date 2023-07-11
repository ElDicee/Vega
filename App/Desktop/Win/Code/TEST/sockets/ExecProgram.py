import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 8999)
s.connect(addr)
try:
    while True:
        msg = input("Data: ")
        if msg.startswith("!"):
            s.sendall(msg[1:].encode())
            resp = s.recv(1024)
            if resp:
                print(resp.decode())
except KeyboardInterrupt:
    s.close()