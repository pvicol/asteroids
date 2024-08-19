.PHONY: clean
clean:
	find . -name \*.pyc -delete
	rm -rf venv/ bin/ lib/ include/ pyvenv.cfg share/

.PHONY: install
install:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

.PHONY: lint
lint:
	. venv/bin/activate && flake8 game/ tests/

.PHONY: test
unit-tests:
	. venv/bin/activate && python -m pytest tests/unit
