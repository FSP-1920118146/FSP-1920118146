import ssl
import socket

hostname = 'google.com'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print("TLS Version :", ssock.version())
        print("Cipher Suite:", ssock.cipher())
