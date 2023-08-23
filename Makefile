init:
	source .venv/bin/activate
	python -m pip install -U pip
	python -m pip install -r requirements.txt

sphinx-docs:
	cd docs/ && \
		sphinx-apidoc -f -o . .. ../setup.py && \
		$(MAKE) html

clean-sphinx-docs:
	find docs -type f ! -name '[mM]ake*' ! -name 'index.rst' ! -name 'conf.py' ! -path "./docs/_static/*" ! -path "./docs/_templates/*" -delete
