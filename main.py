import socket
import ssl
import os
import dns.message
import dns.name
import dns.query



working_path = os.getcwd()

listen_addr = ''
listen_port = 1853
server_cert = working_path + "/keys/server.crt"
server_key = working_path + "/keys/server.key"

host_name = '1.1.1.1'
host_port = 853

#host_name = 'localhost'
#host_port = 18082

# local_ca_folder = working_path + "/keys/local_ca/"
# server_crt_file_name = local_ca_folder + host_name+".crt"

client_cert = working_path + "/keys/client.crt"
client_key = working_path + "/keys/client.key"

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

#####
context_client = ssl.create_default_context()
# context_client.load_verify_locations(server_crt_file_name)
#context_client.load_cert_chain(certfile=client_cert, keyfile=client_key)
#context_client.load_verify_locations(client_cert)
####
# context_client = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context_client.verify_mode = ssl.CERT_REQUIRED
# context_client.load_cert_chain(server_cert, server_key)
# context_client = ssl.create_default_context()
# context_client.load_cert_chain(certfile=client_cert, keyfile=client_key)
#
# ClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# conn = context_client.wrap_socket(ClientSocket, server_side=False, server_hostname=host_name)
####

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as sock:
    sock.bind((listen_addr, listen_port))

    while True:

        #data, addr = sock.recvfrom(4096)  # buffer size is 1024 bytes
        data = dns.query.receive_udp(sock)
        #print(data[2])
        #print(data[0], type(data))
        with context_client.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host_name) as tls:
                tls.connect((host_name, host_port))
                #print(f'Client say:', data[0], data[1], '\n')
                dns.query.send_tcp(tls, data[0])

                data_tls = dns.query.receive_tcp(tls)
                #print(f'Server say:', data_tls[0], data_tls[1], '\n')
                #print(type(data[0]))
                dns.query.send_udp(sock, data_tls[0], data[2])


                tls.close()
                sock.close()

        # conn = context_client.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0), \
        #                                   server_hostname=host_name)
        #conn.connect((host_name, host_port))
        #conn.do_handshake()

        # print(conn.version())
        # conn.sendall(data)

        # client_data = conn.recv(1024)
        # print("received message from tls: %s" % client_data)
        # sock.send(client_data)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
#     sock.bind(('127.0.0.1', 8443))
#     sock.listen(5)
#     with context.wrap_socket(sock, server_side=True) as ssock:
#         conn, addr = ssock.accept()


# import socket
# #from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
# import ssl
# import os
#
# working_path = os.getcwd()
#
#
# listen_addr = '127.0.0.1'
# listen_port = 18082
#
# server_cert = working_path + "/keys/server.crt"
# server_key = working_path + "/keys/server.key"
# client_cert = working_path + "/keys/client.crt"
#
# print(1)
# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# print(2)
# context.verify_mode = ssl.CERT_REQUIRED
# print(3)
# context.load_cert_chain(certfile=server_cert, keyfile=server_key)
# print(4)
# context.load_verify_locations(cafile=client_cert)
# print(5)
#
# bindsocket = socket.socket()
# print(6)
# bindsocket.bind((listen_addr, listen_port))
# print(7)
# bindsocket.listen(5)
#



# import socket
# import ssl
# from threading import Thread
# import os
# from time import sleep
#
#
# class SSLServer:
#     def __init__(
#         self, host, port, server_cert, server_key, client_cert, chunk_size=1024
#     ):
#         self.host = host
#         self.port = port
#         self.chunk_size = chunk_size
#         self._context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#         self._context.verify_mode = ssl.CERT_REQUIRED
#         self._context.load_cert_chain(server_cert, server_key)
#         self._context.load_verify_locations(client_cert)
#
#     def connect(self):
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
#             sock.bind((self.host, self.port))
#             sock.listen(5)
#             while True:
#                 conn, _ = sock.accept()
#                 with self._context.wrap_socket(conn, server_side=True) as sconn:
#                     self._recv(sconn)
#
#     def _recv(self, sock):
#         while True:
#             data = sock.recv(self.chunk_size)
#             if data:
#                 print(data.decode())
#             else:
#                 break
#
#
# class SSLServerThread(Thread):
#     def __init__(self, server):
#         super().__init__()
#         self._server = server
#         self.daemon = True
#
#     def run(self):
#         self._server.connect()
#
#
# working_path = os.getcwd()
# server_host = "localhost"
# server_port = 11234
# client_cert = working_path + "/keys/client_cert.pem"
# client_key = working_path + "/keys/client_key.pem"
# server_cert = working_path + "/keys/server_cert.pem"
# server_key = working_path + "/keys/server_key.pem"
#
# #print(client_cert, client_key)
#
# s = SSLServer(server_host, server_port, server_cert, server_key, client_cert)
#
# s.connect()
# # print(2)
# # s_thread = SSLServerThread(s)
# # print(3)
# # s_thread.start()
# #
# # while 1:
# #     print()
# # import socket, ssl, os
# # working_path = os.getcwd()
# #
# # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# # context.load_cert_chain(certfile=working_path + '/keys/server_cert.pem',
# #                         keyfile=working_path + '/keys/server_key.pem')
# #
# # bindsocket = socket.socket()
# # bindsocket.bind(('', 2099))
# # bindsocket.listen(5)
# #
# # while True:
# #     newsocket, fromaddr = bindsocket.accept()
# #     sslsoc = context.wrap_socket(newsocket, server_side=True)
# #     request = sslsoc.read()
# #     print(request)
#
#
# # import socket
# # import ssl
# # import os
# #
# # working_path = os.getcwd()
# #
# # #context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# # #context.load_cert_chain(working_path + '/keys/server_cert.pem', working_path + '/keys/server_key.pem')
# #
# # with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
# #     sock.bind(("127.0.0.1", 65432))
# #     sock.listen()
# #     conn, addr = sock.accept()
# #     with conn:
# #         print(f"Connected by {addr}")
# #         while True:
# #             data = conn.recv(1024)
# #             if not data:
# #                 break
# #             conn.sendall(data)
# #     # with context.wrap_socket(sock, server_side=True) as ssock:
# #
# #
# #
# # # cert = ssl.get_server_certificate(addr=["1.1.1.1", 853])
# #
# # #print(cert)
# #
# # # hostname = '1.1.1.1'
# # # context = ssl.create_default_context()
# #
# # # with socket.create_connection((hostname, 853)) as sock:
# # #     with context.wrap_socket(sock, server_hostname=hostname) as ssock:
# # #         print(ssock.version())
# #
# #
# #
# #
# #
