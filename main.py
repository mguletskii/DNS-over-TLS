import dnstlsgtw


listen_addr = ''
listen_port = 1853

host_name = '1.1.1.1'
host_port = 853

gtw = dnstlsgtw.dnstlsgtw(listen_addr, listen_port, host_name, host_port)
