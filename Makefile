build:
	@python setup.py sdist bdist_wheel

upload:
	@twine upload dist/*

build_cleanup:
	@rm -rf dist build django_extreme_tdd.egg-info

clean:
	@find . -name *.pyc -delete
