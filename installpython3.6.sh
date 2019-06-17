#!/usr/bin/env bash

echo 'disable firewalld'
sleep 3
systemctl stop firewalld
systemctl disable firewalld


## installation required GCC
echo 'installation required GCC'
sleep 4
yum install gcc openssl-devel bzip2-devel wget -y

## Download Python

echo 'Download Python'

sleep 4
cd /usr/src
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz

## Extract
tar xzf Python-3.6.8.tgz

# make and install

echo 'make and install'

sleep 4
cd Python-3.6.8
./configure --enable-optimizations
make altinstall

rm -f /usr/src/Python-3.6.8.tgz

echo 'python3.6 -V'

chmod -R +x /root/vsftp/*.py

/root/vsftp/vsftp.py
