import socket

# print(socket.gethostbyname(socket.gethostname()))

# 不同的主機會抓到不一樣的值
addrs = socket.getaddrinfo(socket.gethostname(),None)
for addr in addrs:
    print(addr)

# print(socket.getaddrinfo(socket.gethostname(),None)[3][4][0])

# 可以準確抓到本機ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])