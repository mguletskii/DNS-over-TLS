# DNS-over-TLS

## Running

Gateway for converting **DNS** requests to **DNS over TLS** requests.

I used dnspython library. Application just redirects the queries between **DNS** and **DNS over TLS** servers.
Any query start a new thread and call **dnstlsgtw** class instance.

To run container, use a **Compose**:

```
cd ~/
git clone https://github.com/mguletckii/DNS-over-TLS-Challenge.git
cd ~/DNS-over-TLS-Challenge/
docker compose up -d
```

To build a container image, use a **Dockerfile**:

```
cd ~/
git clone https://github.com/mguletckii/DNS-over-TLS-Challenge.git
cd ~/DNS-over-TLS-Challenge/
docker build -t dnstls .
```

Run container, from **image**:
Container from **Dockerfile** build image:
```
docker run -d -p 1853:1853/udp dnstls
```
Or you may use **docker hub** image:
```
docker run -d -p 1853:1853/udp mguletskii/dnstls
```

## Testing

For testing multi connection feature, I used the simple **BASH** script.

```
#!/bin/bash

for ((i=1; i<=$3; i++))
do
    dig @$1 -p $2 aws.amazon.com &
    dig @$1 -p $2 google.com &
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
    dig @\$1 -p \$2 aws.amazon.com & \n \
    dig @\$1 -p \$2 google.com & \n \
done \n \
\n \
wait" >> ~/dnstest.sh

chmod +x ~/dnstest.sh
```

For start test:

```
~/dnstest.sh 172.25.192.1 1853 2
```

Where:
```
172.25.192.1 - Server IP where work application
1853 - application port
2 - how many loops will be done
```

