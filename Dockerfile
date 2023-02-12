FROM python:3.10.0

WORKDIR /app

COPY main.py requirements ./
	 
RUN pip install --no-cache-dir -r requirements

ENTRYPOINT ["python","-u","./main.py"]

EXPOSE 1853/udp