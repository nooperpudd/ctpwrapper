clean:
	python3 setup.py clean
	rm -rf build dist
	rm -f .ctpwrapper/*.so
	rm -f .ctpwrapper/TraderApi.cpp
	rm -f .ctpwrapper/MdApi.cpp

.PHONY: build
build: clean
	python3 setup.py build_ext --inplace

docker:
	docker build -t ctpwrapper .

start:
	docker run -it --rm --name=ctpwrapper ctpwrapper /bin/bash
