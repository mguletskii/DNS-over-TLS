FROM python:3.7-alpine

WORKDIR /app

COPY requirements ./
	 
RUN pip install --no-cache-dir -r requirements

COPY main.py dnstlsgtw.py ./

EXPOSE 1853/udp

ENTRYPOINT ["python"]

CMD ["main.py","-a 0.0.0.0","-p 1853","-A 1.1.1.1","-P 853"]

