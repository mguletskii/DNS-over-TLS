FROM python:3.10.0

WORKDIR /app

COPY main.py dnstlsgtw.py requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENV LIST_HOST=0.0.0.0 \
    LIST_PORT=1853 \
    DNSTLS_HOST=1.1.1.1 \
    DNSTLS_PORT=853 

ENTRYPOINT ["python","-u","./main.py"]

EXPOSE 1853/udp