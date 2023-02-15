FROM python:3.7-alpine

WORKDIR /app

COPY main.py dnstlsgtw.py requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENTRYPOINT ["python"]

CMD ["main.py","-a 0.0.0.0","-p 1853","-A 1.1.1.1","-P 853"]

EXPOSE 1853/udp