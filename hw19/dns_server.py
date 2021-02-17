import socket


IP = "127.0.0.1"
PORT = 53
BUFFER_SIZE = 512

NAME_TABLE = {"google.com": "228.228.228.228"}


class WrongHostName(Exception):
    pass


class BadRequest(Exception):
    pass


def main():
    # Create a datagram socket
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind ip and port
    udp_sock.bind((IP, PORT))

    # Listen income datagrams
    while True:
        data_bytes = udp_sock.recvfrom(BUFFER_SIZE)
        message, address = data_bytes[0], data_bytes[1]

        try:
            params = message.decode().split(' ')

            if params[0] == 'A':
                if params[1] in NAME_TABLE.keys():
                    print(f"Request from {str(address)} for {params[1]}")
                    udp_sock.sendto(NAME_TABLE[params[1]].encode(), address)
                else:
                    raise WrongHostName
            elif params[0] == 'ADD':
                NAME_TABLE.update({params[1]: params[2]})
                print(f"Adding ip {params[2]} for {params[1]}")
                client_msg = f"IP {params[2]} for {params[1]} was successfully added"
                udp_sock.sendto(client_msg.encode(), address)
            else:
                raise BadRequest

        except WrongHostName:
            err_message = f"Can't find ip_address for {params[1]}"
            print(err_message)
            udp_sock.sendto(err_message.encode(), address)

        except BadRequest:
            err_message = f"Bad request: {str(message)}"
            print(err_message)
            udp_sock.sendto(err_message.encode(), address)

        except Exception:
            err_message = "Something went wrong!"
            print(err_message)
            udp_sock.sendto(err_message.encode(), address)


if __name__ == '__main__':
    main()
