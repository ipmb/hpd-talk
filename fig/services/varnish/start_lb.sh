#!/bin/bash

ulimit -n 131072
#ulimit -l 82000

echo "import directors;" > /etc/varnish/backends.vcl
# setup varnish for up to 10 possible web containers
for i in {1..20}; do
    BACKEND="WEB_${i}_NAME"
    if [ -n "${!BACKEND}" ]; then
        cat <<EOT >> /etc/varnish/backends.vcl
backend web_$i {
    .host = "${!BACKEND}";
    .host_header = "example.com";
    .port = "8080";
}
EOT
    fi
done

echo "sub vcl_init {new lb = directors.round_robin();" >> /etc/varnish/backends.vcl

for i in {1..20}; do
    BACKEND="WEB_${i}_NAME"
    if [ -n "${!BACKEND}" ]; then
        echo "lb.add_backend(web_$i);" >> /etc/varnish/backends.vcl
    fi
done
echo "}" >> /etc/varnish/backends.vcl

echo "set req.backend_hint = lb.backend();" > /etc/varnish/backend_hint.vcl


cat /etc/varnish/backends.vcl

varnishd -F -a :8080 -T localhost:6082 \
         -f /etc/varnish/default.vcl \
         -S /etc/varnish/secret \
         -s malloc,256m
