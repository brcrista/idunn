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

.venv:
	$(PYTHON) -m venv $@
	source $@/bin/activate && $(PYTHON) -m pip install --upgrade pip && $(PIP) install -r requirements.txt

.PHONY: build
build:
	$(PYTHON) setup.py build

.PHONY: sdist
sdist:
	$(PYTHON) setup.py sdist

.PHONY: install
install:
	$(PIP) install .

.PHONY: uninstall
uninstall:
	$(PIP) uninstall idunn --yes
