import socket
c = socket.socket()
c.connect(('localhost', 9999))

print(c.recv(1024).decode())
# import socket
# ip = socket.gethostbyname('www.google.com')
# print(ip)