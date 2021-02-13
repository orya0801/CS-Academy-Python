import ipaddress as ip
from functools import wraps


def add_ip_address_decorator(add_ip_address):
    @wraps(add_ip_address)
    def wrapper(self, ip_address, interface_name):
        res = f"Adding ip-address {ip_address} {interface_name}"

        try:
            add_ip_address(self, ip_address, interface_name)
        except Exception:
            res += " - exception"
        finally:
            print(res)

    return wrapper


def remove_ip_address_decorator(remove_ip_address):
    @wraps(remove_ip_address)
    def wrapper(self, ip_address_str):
        ip_address = remove_ip_address(self, ip_address_str)

        if ip_address is not None:
            print(f"Removing ip-address {ip_address[1]} {ip_address[0]}")
        else:
            print("The specified ip address is not bound to any interface")

    return wrapper


def add_route_decorator(add_route):
    @wraps(add_route)
    def wrapper(self, ip_addr, gateway):
        res = add_route(self, ip_addr, gateway)
        str_res = f"Adding route to {ip_addr} through {gateway} - "

        if res is not None:
            str_res += "ok"
        else:
            str_res += "exception"

        print(str_res)

    return wrapper


def remove_route_decorator(remove_route):
    @wraps(remove_route)
    def wrapper(self, network_ip):
        res = f"Removing route to {network_ip} "
        route = remove_route(self, network_ip)

        if route is None:
            print(f"{res}- exception")

    return wrapper


class Router:

    def __init__(self):
        # Элементы списка -  [[<interface_name>, <ip_address>], ...]
        self.ip_addresses = []
        # Элементы списка -  [[network_ip, connection_ip_address], ...]
        self.routes = []

    @add_ip_address_decorator
    def add_ip_address(self, ip_address_str, interface_name):
        ip_address = ip.IPv4Interface(ip_address_str)

        # Проверка на занятость интерфейса и ip-адреса
        if interface_name not in [el[0] for el in self.ip_addresses] \
                and ip_address.ip not in [el[1] for el in self.ip_addresses]:
            self.ip_addresses.append([interface_name, ip_address.ip])
            # Добавляем маршрут к непосредственно подключенной сети
            self.routes.append([ip_address.network, ip_address.ip])
        else:
            raise Exception

    @remove_ip_address_decorator
    def remove_ip_address(self, ip_address):
        try:
            ip_addr = [x[1] for x in self.ip_addresses].index(ip.IPv4Interface(ip_address).ip)

            return self.ip_addresses.pop(ip_addr)

        except ValueError:
            return None

    def show_ip_addresses(self):
        print("\nIP Addresses:\nIF:\t\tIP:")

        for elem in self.ip_addresses:
            print(f"{elem[0]}\t{elem[1]}")
        print()

    @add_route_decorator
    def add_ip_route(self, ip_address_str, gateway_str):
        gateway = ip.ip_address(gateway_str)
        ip_address = ip.ip_network(ip_address_str)

        for elem in self.routes:
            hosts = list(elem[0].hosts())
            if gateway in hosts and gateway != elem[1]:
                self.routes.append((ip_address, gateway))

                return [ip_address, gateway]

    @remove_route_decorator
    def remove_ip_route(self, network_ip_str):
        network_ip = ip.ip_network(network_ip_str)

        try:
            i = [x[0] for x in self.routes].index(network_ip)
            return self.routes.pop(i)
        except ValueError:
            return None

    def show_ip_routes(self):
        print("IP Routes:\nNum:\tIPRANGE:\t\t\tNextHopIPAddress")

        for elem in enumerate(self.routes):
            print(f"{elem[0] + 1}:\t\t{elem[1][0]}\t\t{elem[1][1]}")
