#!/bin/bash

ulimit -n 131072
#ulimit -l 82000


cat <<EOT >> /etc/varnish/backends.vcl
    backend default {
        .host = "web_1";
        .host_header = "example.com";
        .port = "8080";
        .probe = {
            .url = "/probe/";
            .interval = 10s;
            .timeout = 2s;
            .window = 5;
            .threshold = 3; }
    }
EOT
    echo "# not required for single backend" > /etc/varnish/backend_hint.vcl

cat /etc/varnish/backends.vcl

varnishd -F -a :6081 -T localhost:6082 \
         -f /etc/varnish/default.vcl \
         -S /etc/varnish/secret \
         -s malloc,256m
