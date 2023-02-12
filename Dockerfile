FROM python:3.10.0

WORKDIR /app

COPY main.py dnstlsgtw.py requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENV DNSTLS_HOST=1.1.1.1
ENV DNSTLS_PORT=853
ENV LIST_HOST=0.0.0.0
ENV LIST_PORT=1853

ENTRYPOINT ["python","-u","./main.py"]

EXPOSE 1853/udp