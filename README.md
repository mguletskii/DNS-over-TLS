# DNS-over-TLS

## Running

Gateway for converting **DNS** requests to **DNS over TLS** requests.

I used dnspython library. Application just redirects the queries between **DNS** and **DNS over TLS** servers.
Any query start a new thread and call **dnstlsgtw** class instance.

To run container, use a **Compose**:

```
cd ~/
git clone https://github.com/mguletckii/DNS-over-TLS.git
cd ~/DNS-over-TLS/
docker compose up -d
```

To build a container image, use a **Dockerfile**:

```
cd ~/
git clone https://github.com/mguletckii/DNS-over-TLS.git
cd ~/DNS-over-TLS/
docker build -t dnstls .
```

**ENV** Variables:
```
LIST_HOST - Local server address binding (0.0.0.0 by default)
DNSTLS_HOST - DNS over TLS server host (1.1.1.1 by default)
DNSTLS_PORT - DNS over TLS server port (853 by default)
```

Run container, from **image**:
Container from **Dockerfile** build image:
```
docker run -d -p 1853:53/udp dnstls
```
Or you may use **docker hub** image:
```
docker run -d -p 1853:53/udp mguletskii/dnstls
```

## Testing

For basic test you may use **dig**:

```
dig @localhost -p1853 google.com
```

For multi connection testing I used **kdig** util from knot-dnsutils.

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
~/dnstest.sh localhost 1853 2
```

Where:
```
localhost - Server IP where work application
1853 - application port
2 - how many loops will be done
```

