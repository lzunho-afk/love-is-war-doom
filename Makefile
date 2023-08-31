PY_INST=python -m pip install -U

release: init sphinx-docs
	$(PY_INST) pyinstaller
	pyinstaller loveiswar.py
	cp -r ./docs/_build/ ./dist/loveiswar/docs/
	cp -r ./loveiswar/ ./dist/loveiswar/src/
	cp -r ./assets/ ./dist/loveiswar/
	cp ./LICENSE ./README.rst ./dist/loveiswar/

init:
	$(PY_INST) pip
	$(PY_INST) -r requirements.txt

sphinx-docs: clean-sphinx-docs
	cd docs/ && \
		sphinx-apidoc -MPfe -o . .. ../setup.py ../loveiswar.py && \
		$(MAKE) html

clean-sphinx-docs:
	find docs -type f ! -name '[mM]ake*' ! -name 'index.rst' ! -name 'conf.py' ! -path "./docs/_static/*" ! -path "./docs/_templates/*" -delete

clean-cache:
	find loveiswar -type d -name '__pycache__' -exec rm -r "{}" \;
