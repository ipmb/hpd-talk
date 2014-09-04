#!/bin/bash

WEB1=10.0.0.18
WEB2=10.0.0.17
LB=10.0.0.19
DB_URL=postgres://hpd:hpd-talk@hpd.xxxxx.us-east-1.rds.amazonaws.com:5432/hpd

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
echo "deb https://get.docker.io/ubuntu docker main" > /etc/apt/sources.list.d/docker.list
apt-get update
apt-get -y dist-upgrade
apt-get -y install lxc-docker python-setuptools htop
gpasswd -a ubuntu docker
docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter
(cd /; easy_install -U fig)
echo "$1" > /etc/hostname
hostname "$1"
grep "web1" /etc/hosts || echo -e "$WEB1 web1\n$WEB2 web2\n$LB lb" >> /etc/hosts

cat <<EOT > /home/ubuntu/.bash_aliases
export DATABASE_URL=$DB_URL
export WEB_1_NAME=`getent hosts web1 | cut -f1 -d' ' | head -n1`
export WEB_2_NAME=`getent hosts web2 | cut -f1 -d' ' | head -n1`
EOT
