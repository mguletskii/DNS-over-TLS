FROM python:3.7-alpine

WORKDIR /app

COPY requirements ./
	 
RUN pip install --no-cache-dir -r requirements

EXPOSE 1853/udp

COPY main.py dnstlsgtw.py ./

ENTRYPOINT ["python"]

CMD ["main.py","-a 0.0.0.0","-p 1853","-A 1.1.1.1","-P 853"]

