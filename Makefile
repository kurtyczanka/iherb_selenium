PHONY: test

deps:
	pip install -r requirements.txt

test:
	python3 -m unittest