import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("localhost", 7773)
    s.connect(addr)
    try:
        msg = input("Data: ")
        if msg.startswith("!"):
            s.sendall(msg[1:].encode())
            resp = s.recv(1024)
            if resp:
                print(resp.decode())
    except KeyboardInterrupt:
        s.close()