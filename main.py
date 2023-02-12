import dnstlsgtw
<<<<<<< HEAD
=======
import socket, dns.query
import threading
>>>>>>> DNS_over_TLS


listen_addr = ''
listen_port = 1853

host_name = '1.1.1.1'
host_port = 853

<<<<<<< HEAD
connection_threads = []

gtw = dnstlsgtw.dnstlsgtw(listen_addr, listen_port, host_name, host_port)
=======
connection_threads = list()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((listen_addr, listen_port))

while True:
    new_thread = threading.Thread(target=dnstlsgtw.dnstlsgtw, args=(host_name, host_port, sock, \
        dns.query.receive_udp(sock)))
    connection_threads.append(new_thread)
    new_thread.start()
>>>>>>> DNS_over_TLS
