FROM python:3.6
RUN pip3 install cython pip setuptools --upgrade
WORKDIR /code
