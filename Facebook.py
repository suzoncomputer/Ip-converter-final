
import socket
import pyfiglet
banner = pyfiglet.figlet_format("Domain Name")
print(banner)

domain_name = input("Enter Your Name:")
ip = socket.gethostbyname(domain_name)
print(ip)