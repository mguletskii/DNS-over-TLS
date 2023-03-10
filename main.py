from dnstlsgtw import dnstlsgtw
import os,socket, dns.query
import threading

#Default configuration
#/////////////////
DEF_LIST_HOST = '0.0.0.0'
DEF_LIST_PORT = '53'
DEF_DNSTLS_HOST = '1.1.1.1'
DEF_DNSTLS_PORT = '853'
#////////////////

try:
    listen_addr = str(os.environ['LIST_HOST'])
    listen_port = int(os.environ.get['LIST_PORT', DEF_LIST_PORT])
    host_name = str(os.environ['DNSTLS_HOST'])
    host_port = int(os.environ['DNSTLS_PORT'])
except:
    from argparse import ArgumentParser

    args_parser = ArgumentParser()

    args_parser.add_argument('--address','-a', required=False, help='Local server address binding', default=DEF_LIST_HOST, type=str)
    args_parser.add_argument('--port','-p', required=False, help='Local server port', default=DEF_LIST_PORT, type=int)
    args_parser.add_argument('--dnshost','--dh','-A', required=False, help='DNS over TLS host', default=DEF_DNSTLS_HOST, type=str)
    args_parser.add_argument('--dnsport','--dp','-P', required=False, help='DNS over TLS port', default=DEF_DNSTLS_PORT, type=int)

    args = args_parser.parse_args()

    listen_addr = args.address.strip()
    listen_port = args.port
    host_name = args.dnshost.strip()
    host_port = args.dnsport

connection_threads = list()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((listen_addr, listen_port))

while True:
    new_thread = threading.Thread(target=dnstlsgtw, args=(host_name, host_port, sock, \
        dns.query.receive_udp(sock)))
    connection_threads.append(new_thread)
    new_thread.start()
