PIP := pip3
PYTHON := python3

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
	$(PYTHON) setup.py build

.PHONY: sdist
sdist:
	$(PYTHON) setup.py sdist

.PHONY: install
install:
	$(PYTHON) setup.py install

.PHONY: uninstall
uninstall:
	$(PIP) uninstall idunn --yes