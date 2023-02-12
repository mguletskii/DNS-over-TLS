import dns.query, socket, ssl

class dnstlsgtw:
 
    def __init__(self, dns_host: str, dns_port: str, dnstls_host: str, dnstls_port: int):
        self.dns_host = dns_host
        self.dns_port = dns_port
        self.tls_host = dnstls_host
        self.tls_port = dnstls_port
        self.context_client = ssl.create_default_context()
        self.__get_dnstls()

    def __get_dnstls(self):
        self.__binding_dns()
        while True:
            self.__recv_dns()
            self.__connect_dnstls()
            self.__send_dnstls()
            self.__recv_dnstls()
            self.__send_dns()
            self.__close_dnstls()
        self.__close_dns()

    def __binding_dns(self):
        try:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            self.__sock.bind((self.dns_host, self.dns_port))
        except Exception as e:
            print("ERROR! dnstlsgtw Connecting DNS:", str(e))

    def __close_dns(self):
        try:
            self.__sock.close()
        except Exception as e:
            print("ERROR! dnstlsgtw Closing DNS:", (self.dns_host, self.dns_port), " ", str(e))
    
    def __recv_dns(self):
        try:
            self.__recv_dns_data = dns.query.receive_udp(self.__sock)
        except Exception as e:
            print("ERROR! dnstlsgtw Receaving:", str(e))

    def __connect_dnstls(self):
        try:
            self.__sock_tls = self.context_client.wrap_socket(socket.socket(socket.AF_INET), \
            server_hostname=self.tls_host)
            try:
                self.__sock_tls.connect((self.tls_host, self.tls_port))
            except Exception as e:
                print("ERROR! dnstlsgtw Connection to TLS host:", (self.tls_host, self.tls_port), " ", str(e))
        except Exception as e:
            print("ERROR! dnstlsgtw Creating TLS socket:", str(e))

    
    def __send_dnstls(self):
        try:
            dns.query.send_tcp(self.__sock_tls, self.__recv_dns_data[0])
        except Exception as e:
            print("ERROR! dnstlsgtw Sending to DNSTLS:", (self.tls_host, self.tls_port), " ", str(e))


    def __recv_dnstls(self):
        try:
            self.__recv_dnstls_data = dns.query.receive_tcp(self.__sock_tls)
        except Exception as e:
            print("ERROR! dnstlsgtw Receaving to DNSTLS:", (self.tls_host, self.tls_port), " ", str(e))

    def __send_dns(self):
        try:
            dns.query.send_udp(self.__sock, self.__recv_dnstls_data[0], self.__recv_dns_data[2])
        except Exception as e:
            print("ERROR! dnstlsgtw Sending DNS:", self.__recv_dns_data[2], " ", str(e))

    def __close_dnstls(self):
        try:
            self.__sock_tls.close()
        except Exception as e:
            print("ERROR! dnstlsgtw Closing DNSTLS:", (self.tls_host, self.tls_port), " ", str(e))
