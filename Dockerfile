FROM registry.docker-cn.com/library/python:3.6.3

RUN echo "Asia/Shanghai" > /etc/timezone

RUN dpkg-reconfigure -f noninteractive tzdata

ADD ./ctpwrapper /ctpwrapper

WORKDIR /ctpwrapper

RUN python setup.py build
