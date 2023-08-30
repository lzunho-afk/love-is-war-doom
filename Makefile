PY_INST=python -m pip install -U

init:
	source .venv/bin/activate && \
		$(PY_INST) pip && \
		$(PY_INST) -r requirements.txt

sphinx-docs:
	cd docs/ && \
		sphinx-apidoc -M -f -o . .. ../setup.py && \
		$(MAKE) html

clean-sphinx-docs:
	find docs -type f ! -name '[mM]ake*' ! -name 'index.rst' ! -name 'conf.py' ! -path "./docs/_static/*" ! -path "./docs/_templates/*" -delete
