import dnstlsgtw
import socket, dns.query
import threading
import sys


try:
    listen_addr = sys.argv[1]
    listen_port = int(sys.argv[2])
    host_name = sys.argv[3]
    host_port = int(sys.argv[4])
except:
    print("ERROR! In command line arguments!", sys.argv[1:])
    exit()

connection_threads = list()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((listen_addr, listen_port))

while True:
    new_thread = threading.Thread(target=dnstlsgtw.dnstlsgtw, args=(host_name, host_port, sock, \
        dns.query.receive_udp(sock)))
    connection_threads.append(new_thread)
    new_thread.start()
