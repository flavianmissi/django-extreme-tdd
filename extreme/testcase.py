"""
Available TestCase implementations.

Only use this test case if you are under Django 1.8.
It is not recommended for Django 1.8 because they fixed the issue their TestCase
had with writing in the database on the setUpClass and TearDownClass, which
finally makes things really faster on that version :)
"""
from django.test import TransactionTestCase
from .cleanup import truncate_tables


class TestCase(TransactionTestCase):
    """
    TestCase provides all Django's customs assertion methods.
    By inheriting from TransactionTestCase and overriding its setup and
    teardown primary functions, we remove the transaction load.
    """

    @classmethod
    def setUpClass(cls):
        truncate_tables()

    @classmethod
    def tearDownClass(cls):
        truncate_tables()

    def _pre_setup(self):
        """
        Overriding from TransactionTestCase so it doesn't do it's black magic.
        """
        pass

    def _post_teardown(self):
        """
        Same as above.
        """
        pass
