from router import Router

r1 = Router()
r1.add_ip_address('192.168.5.14/24', "eth1")
r1.add_ip_address('192.168.5.14/24', "eth2")
r1.add_ip_route('172.16.0.0/16', '192.168.5.1') # ok
r1.add_ip_route('172.16.0.0/16', '172.168.8.1') # exception
r1.add_ip_route('172.24.0.0/16', '172.16.8.1')  # ok

r1.show_ip_addresses()
r1.show_ip_routes()