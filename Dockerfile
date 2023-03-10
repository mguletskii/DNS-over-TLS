FROM python:3.7-alpine

WORKDIR /app

COPY requirements ./
	 
RUN pip install --no-cache-dir -r requirements

EXPOSE 1853/udp

ENV LIST_HOST=0.0.0.0 \
    LIST_PORT=53 \
    DNSTLS_HOST=1.1.1.1 \
    DNSTLS_PORT=853


COPY main.py dnstlsgtw.py ./

ENTRYPOINT ["python", "main.py"]

#CMD ["main.py","-a 0.0.0.0","-p 53","-A 1.1.1.1","-P 853"]


