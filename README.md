# DNS-over-TLS

Gateway for converting **DNS** requests to **DNS over TLS** requests.

To build a container image, use a **Dockerfile**:

~~~
cd ~/
git clone https://github.com/mguletckii/DNS-over-TLS-Challenge.git
cd ~/DNS-over-TLS-Challenge/
docker build -t dnstls:0.1 .
docker run -d -p 1853:1853/udp dnstls:0.1
~~~

You may configurate it using **ENV** variables or **CMD** arguments:

## CMD (Priority):
~~~
FROM python:3.10.0

WORKDIR /app

COPY main.py dnstlsgtw.py requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENTRYPOINT ["python","-u","./main.py"]
CMD ["0.0.0.0","1853","1.1.1.1","853"]

EXPOSE 1853/udp
~~~

### ENV:
~~~
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
~~~

