FROM python:3.7-alpine

WORKDIR /app

COPY main.py dnstlsgtw.py requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENTRYPOINT ["python","-u"]
CMD ["main.py","0.0.0.0","1853","1.1.1.1","853"]

EXPOSE 1853/udp