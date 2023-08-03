init:
	pip install -r requirements.txt

sphinx-docs:
	cd docs/ && \
		sphinx-apidoc -o . .. && \
		$(MAKE) html

clean-sphinx-docs:
	find docs -type f ! -name '[mM]ake*' ! -name 'index.rst' ! -name 'conf.py' ! -path "./docs/_static/*" ! -path "./docs/_templates/*" -delete
