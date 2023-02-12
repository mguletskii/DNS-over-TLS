# DNS-over-TLS

Gateway for converting **DNS** requests to **DNS over TLS** requests.

I used dnspython library. Application just redirects the queries between **DNS** and **DNS over TLS** servers.
Any query start a new thread and call **dnstlsgtw** class instance.


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

For testing I used kdig util from knot-dnsutils.

~~~
sudo apt install knot-dnsutils
~~~

For testing multi connection feature, I used the simple **BASH** script.

~~~
#!/bin/bash

for i in {1..$3}
do
    kdig -d $1 -p $2 aws.amazon.com &
    kdig -d $1 -p $2 google.com &
done

wait
~~~

You may create this file, with his a couple commands:

~~~
printf '#!/bin/bash' > ~/test1.sh
echo -e \
"\n \n \
for i in {1..\$3} \n \
do \n \
    kdig -d \$1 -p \$2 aws.amazon.com & \n \
    kdig -d \$1 -p \$2 google.com & \n \
done \n \
\n \
wait" >> ~/test.sh

chmod +x ~/test.sh
~~~

For start test:

~~~
~/test1.sh 172.25.192.1 1853 2
~~~

Where:
~~~
172.25.192.1 - Server IP where work application
1853 - application port
2 - how many loops will be done
~~~

# QA

## Imagine this proxy being deployed in an infrastructure. What would be the security concerns you would raise?
~~~
Close 53 output port, for prevent all unprotected requests.
Data validity. For increase security I would compare DNS records between 2 or more random selected servers.
Use configured pod network (if it's work on the one pod) or configure service CIDR for one VPS.
~~~

## How would you integrate that solution in a distributed, microservices-oriented and containerized architecture?

~~~
This container is ephemeral.
I would use docker registry or ECR to integrate with kubernetes or ECS.
~~~

## What other improvements do you think would be interesting to add to the project?

~~~
Add support of many DNSoverTLS servers, for increase the stability and security of service. 
Add cache with configuring TTL.
~~~
