import socket
import ssl
import os
import dns.query


working_path = os.getcwd()

listen_addr = ''
listen_port = 1853

host_name = '1.1.1.1'
host_port = 853

context_client = ssl.create_default_context()


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as sock:
    sock.bind((listen_addr, listen_port))

    while True:
        data = dns.query.receive_udp(sock)
        with context_client.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host_name) as tls:
                tls.connect((host_name, host_port))
                dns.query.send_tcp(tls, data[0])

                data_tls = dns.query.receive_tcp(tls)
                dns.query.send_udp(sock, data_tls[0], data[2])

                tls.close()
                sock.close()
