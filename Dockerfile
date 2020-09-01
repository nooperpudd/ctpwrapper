FROM python:3.8
RUN pip3 install cython pip setuptools --upgrade
WORKDIR /code
