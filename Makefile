build:
	@python setup.py sdist bdist_wheel

upload: build_cleanup
	@twine upload dist/*

build_cleanup:
	@rm -rf dist

clean:
	@find . -name *.pyc -delete
