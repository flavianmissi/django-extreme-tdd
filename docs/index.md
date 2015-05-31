# Django eXtreme TDD Documentation


## Installation

#### From pip

    $ pip install django-extreme-tdd

#### From source

    $ python setup.py install

## Usage

Just inherit from `extreme.TestCase` instead of `django.test.TestCase`.

    import extreme

    class MyTestCase(extreme.TestCase):

        # ... your tests ...


## Contributing

### Install development dependencies (automatically install testing dependencies as well)

    $ pip install -r requirements_dev.txt

### Running tests

    $ nosetests


## Be aware! Alpha stage!
