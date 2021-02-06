"""
    Написать класс router.
    Должен иметь методы добавить/удалить/вывести список ip address.
    Должен иметь методы добавить/удалить/вывести список ip routes.

    Есть маршруты к непосредственно-подключенным сетям:
    если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
    значит у него должен быть маршрут:
    к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

    Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
    то надо проверять доступен ли gateway.

    Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
    192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

    Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
    до которого у нас пока еще нет маршрута, то должен вылетать exception.

    Например:
    Добавляем ip-address 192.168.5.14/24 eth1.
    Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
    Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
    Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

    Итого - 1 интерфейс и 3 маршрута в таблице.
"""

import ipaddress as ip
from functools import wraps


def add_ip_address_decorator(add_ip_address):
    @wraps(add_ip_address)
    def wrapper(self, ip_address, interface_name):
        print(f"Adding ip-address {ip_address} {interface_name}.")
        add_ip_address(self, ip_address, interface_name)

    return wrapper

def remove_ip_address_decorator(remove_ip_address):
    @wraps(remove_ip_address)
    def wrapper(self, interface_name):
        ip_address = remove_ip_address(self, interface_name)

        if ip_address is not None:
            print(f"Removing ip-address {ip_address} {interface_name}")

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
        route = remove_route(self, network_ip)

        if route is not None:
            print(f"Removing route to {route[0]} through {route[1]}")

    return wrapper


class Router:

    def __init__(self):
        # Словарь формата <interface_name>:<ip_address>
        self.ip_addresses = {}
        # Элементы списка - кортежи формата (network_ip, connection_ip_address)
        # network_ip - сеть, до которой ведет маршрут
        # connection_ip_address - ip адрес маршрутизатора из ip_addresses
        self.routes = []

    @add_ip_address_decorator
    def add_ip_address(self, ip_address, interface_name):
        interface = ip.IPv4Interface(ip_address)

        self.ip_addresses.update({interface_name: interface.ip})
        # Добавляем маршрут к непосредственно подключенной сети
        self.routes.append((interface.network, interface.ip))

    @remove_ip_address_decorator
    def remove_ip_address(self, interface_name):
        try:
            # Поиск маршрута, для которого используется удаляемый ip-адрес
            route = [x[1] for x in self.routes].index(self.ip_addresses[interface_name])
            
            self.routes.pop(route)
            return self.ip_addresses.pop(interface_name)

        except ValueError:
            return None

    def show_ip_addresses(self):
        print("IP Addresses:\nIF:\tIP:")

        for k,v in self.ip_addresses.items():
            print(f"{k}\t{v}")

    @add_route_decorator
    def add_ip_route(self, ip_address_str, gateway_str):
        gateway = ip.ip_address(gateway_str)
        ip_address = ip.ip_network(ip_address_str)

        for elem in self.routes:
            hosts = list(elem[0].hosts())
            if gateway in hosts and gateway != elem[1]:
                self.routes.append((ip_address, gateway))

                return (ip_address, gateway)

    @remove_route_decorator
    def remove_ip_route(self, network_ip_str):
        network_ip = ip.ip_network(network_ip_str)

        try:
            i = [x[0] for x in self.routes].index(network_ip)
            return self.routes.pop(i)
        except ValueError:
            return None
        
    def show_ip_routes(self):
        counter = 1
        print("IP Routes:\nNum:\tIPRANGE:\tNextHopIPAddress")

        for elem in self.routes:
            print(f"{counter}:\t{elem[0]}\t{elem[1]}")
            counter += 1


