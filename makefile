build:
	python3 setup.py build_ext --inplace
clean:
	rm -rf build dist
docker:
	docker build -t ctpwrapper .
start:
	docker run -it --rm --name=ctpwrapper ctpwrapper /bin/bash

