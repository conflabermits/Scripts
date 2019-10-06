FROM ubuntu:18.04

RUN apt-get update
RUN apt-get --assume-yes upgrade

RUN apt-get --assume-yes install \
    python3 \
    dnsutils \
    screen \
    bc \
    bsdmainutils \
    gzip \
    iputils-ping \
    man-db \
    manpages \
    gnupg2 \
    ruby \
    vim \
    emacs \
    nano \
    python \
    python-pip \
    python3-pip \
    apache2 \
    java-common \
    lsb-release \
    curl \
    wget \
    tree

RUN update-alternatives --set editor /usr/bin/vim.basic

RUN curl https://d3pxv6yz143wms.cloudfront.net/8.222.10.1/java-1.8.0-amazon-corretto-jdk_8.222.10-1_amd64.deb -o /tmp/java-1.8.0-amazon-corretto-jdk_8.222.10-1_amd64.deb
RUN dpkg --install /tmp/java-1.8.0-amazon-corretto-jdk_8.222.10-1_amd64.deb

RUN pip install requests
RUN pip3 install requests

