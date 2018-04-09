.PHONY: clean, install, test

install:
	python setup.py install

test:
	python setup.py test

clean:
	rm -rf trellolinker.egg-info .eggs .coverage htmlcov build dist
	find . -name "*.pyc" -exec rm -rf {} \;
