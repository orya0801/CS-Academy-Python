"""
    Test client for dns server. Run after dns_server.
"""

import socket
from dns_server import IP, PORT, BUFFER_SIZE


def main():
    msg1 = str.encode("A google.com")
    msg2 = str.encode("ADD yandex.ru 77.88.21.11")
    msg3 = str.encode("A yandex.ru")

    serverAddressPort = (IP, PORT)

    # Create a UDP socket at client side
    upd_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Request 1
    upd_sock.sendto(msg1, serverAddressPort)

    server_msg, address = upd_sock.recvfrom(BUFFER_SIZE)
    print(server_msg.decode())

    # Request 2
    upd_sock.sendto(msg2, serverAddressPort)

    server_msg, address = upd_sock.recvfrom(BUFFER_SIZE)
    print(server_msg.decode())

    # Request 3
    upd_sock.sendto(msg3, serverAddressPort)

    server_msg, address = upd_sock.recvfrom(BUFFER_SIZE)
    print(server_msg.decode())


if __name__ == '__main__':
    main()