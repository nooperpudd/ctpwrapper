clean:
	python3 setup.py clean --all
	rm -rf build dist
	find ./ctpwrapper/ -name "*.so"  -delete
	find ./ctpwrapper/ -name "*.cpp"  -delete


.PHONY: build-local
build-local: clean
	python3 setup.py build_ext --inplace


.PHONY: build
build: clean
	python3 setup.py build

.PHONY: install
install: clean
	python3 setup.py install
