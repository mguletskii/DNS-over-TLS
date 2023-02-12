import dnstlsgtw
import socket, dns.query
import threading
import os


listen_addr = str(os.environ['LIST_HOST'])
listen_port = int(os.environ['LIST_PORT'])

host_name = str(os.environ['DNSTLS_HOST'])
host_port = int(os.environ['DNSTLS_PORT'])

connection_threads = list()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((listen_addr, listen_port))

while True:
    new_thread = threading.Thread(target=dnstlsgtw.dnstlsgtw, args=(host_name, host_port, sock, \
        dns.query.receive_udp(sock)))
    connection_threads.append(new_thread)
    new_thread.start()
