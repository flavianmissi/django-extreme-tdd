from unittest import TestCase
from mock import patch

import extreme


@patch("extreme.testcase.truncate_tables")
class TestCaseTests(TestCase):

    def test_setUpClass_truncates_tables(self, truncate_mock):
        extreme.TestCase.setUpClass()
        self.assertTrue(truncate_mock.called)
        truncate_mock.assert_called_once()

    def test_tearDownClass_truncates_tables(self, truncate_mock):
        extreme.TestCase.tearDownClass()
        self.assertTrue(truncate_mock.called)
        truncate_mock.assert_called_once()
