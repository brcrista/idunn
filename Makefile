.PHONY: all
all: clean build sdist install

.PHONY: clean
clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -f **/*.pyc
	rm -f *.yml

.PHONY: build
build:
	python setup.py build

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: install
install:
	python setup.py install

.PHONY: uninstall
uninstall:
	pip uninstall idunn --yes