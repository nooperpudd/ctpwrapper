build:
	python setup.py build_ext --inplace
docker:
	docker build -t ctpwrapper .
start:
	docker run -it --rm --name=ctpwrapper ctpwrapper /bin/bash

