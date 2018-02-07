FROM registry.docker-cn.com/library/python:3.6.4

RUN pip3 install cython

ADD . /work

WORKDIR /work


