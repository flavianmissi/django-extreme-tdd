"""
Available TestCase implementations.
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
