import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 8999)
s.bind(addr)

s.listen(1)
try:
    while True:
        client, address = s.accept()
        data = client.recv(1024)
        if data:
            print(data.decode())
            client.sendall("Received".encode())
except KeyboardInterrupt:
    s.close()