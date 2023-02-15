from dnstlsgtw import dnstlsgtw
import socket, dns.query
import threading
from argparse import ArgumentParser

args_parser = ArgumentParser()

args_parser.add_argument('--address','-a',required=False, help='Local server address binding', default='0.0.0.0')
args_parser.add_argument('--port','-p',required=True, help='Local server port', default=1853)
args_parser.add_argument('--dnshost','-dh',required=False, help='DNS over TLS host', default='1.1.1.1')
args_parser.add_argument('--dnsport','-dp',required=False, help='DNS over TLS port', default=853)

args = args_parser.parse_args()

connection_threads = list()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((args.address, int(args.port)))

while True:
    new_thread = threading.Thread(target=dnstlsgtw.dnstlsgtw, args=(args.dnshost, int(args.dnsport), sock, \
        dns.query.receive_udp(sock)))
    connection_threads.append(new_thread)
    new_thread.start()
