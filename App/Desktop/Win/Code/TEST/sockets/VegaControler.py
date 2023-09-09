import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# addr = ("localhost", 8999)
# s.bind(addr)
#
# s.listen(1)
# try:
#     while True:
#         client, address = s.accept()
#         data = client.recv(1024)
#         if data:
#             print(data.decode())
#             client.sendall("Received".encode())
# except KeyboardInterrupt:
#     s.close()


soc = socket.create_server(("127.0.0.1", 7773), family=socket.AF_INET, dualstack_ipv6=False)
soc.listen(99)
while True:
    client, addr = soc.accept()
    data = client.recv(1024)
    if data:
        print(f"{addr}: {data.decode()}")
        client.send("Received".encode())