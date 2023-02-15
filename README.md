# DNS-over-TLS

Gateway for converting **DNS** requests to **DNS over TLS** requests.

I used dnspython library. Application just redirects the queries between **DNS** and **DNS over TLS** servers.
Any query start a new thread and call **dnstlsgtw** class instance.


To build a container image, use a **Dockerfile**:

```
cd ~/
git clone https://github.com/mguletckii/DNS-over-TLS-Challenge.git
cd ~/DNS-over-TLS-Challenge/
docker build -t dnstls:0.1 .
docker run -d -p 1853:1853/udp dnstls:0.1
```

For testing I used kdig util from knot-dnsutils.

```
sudo apt install knot-dnsutils
```

For testing multi connection feature, I used the simple **BASH** script.

```
#!/bin/bash

for ((i=1; i<=$3; i++))
do
    kdig -d $1 -p $2 aws.amazon.com &
    kdig -d $1 -p $2 google.com &
done

wait
```

You may create this file, with his a couple commands:

```
printf '#!/bin/bash' > ~/dnstest.sh
echo -e \
"\n \n \
for ((i=1; i<=\$3; i++)) \n \
do \n \
    kdig -d \$1 -p \$2 aws.amazon.com & \n \
    kdig -d \$1 -p \$2 google.com & \n \
done \n \
\n \
wait" >> ~/dnstest.sh

chmod +x ~/dnstest.sh
```

For start test:

```
~/test1.sh 172.25.192.1 1853 2
```

Where:
```
172.25.192.1 - Server IP where work application
1853 - application port
2 - how many loops will be done
```

