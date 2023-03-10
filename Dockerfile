FROM python:3.7-alpine

WORKDIR /app

COPY requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENV LIST_HOST=0.0.0.0 \
    DNSTLS_HOST=1.1.1.1 \
    DNSTLS_PORT=853

EXPOSE 53/udp

COPY main.py dnstlsgtw.py ./

ENTRYPOINT ["python", "main.py"]

#CMD ["-a 0.0.0.0","-A 1.1.1.1","-P 853"]


