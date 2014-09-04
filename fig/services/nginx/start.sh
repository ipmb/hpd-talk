#!/bin/bash

CONFIG=/etc/upstreams.conf

echo "upstream uwsgicluster {" >> $CONFIG

# setup nginx for up to 20 possible web containers
for i in {1..20}; do
    BACKEND="WEB_${i}_NAME"
    if [ -n "${!BACKEND}" ]; then
        echo "server ${!BACKEND}:8080;" >> $CONFIG
    fi
done

echo "}" >> $CONFIG

cat $CONFIG

nginx
