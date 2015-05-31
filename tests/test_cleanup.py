from unittest import TestCase, skip
from mock import patch, MagicMock
from extreme.cleanup import truncate_tables


class CleanUpTests(TestCase):

    @skip("for now")
    @patch("extreme.cleanup.connections")
    def test_truncate_tables(self, connections_mock):
        cursor_mock = MagicMock()
        connections_mock.__getitem__.return_value.cursor.return_value = cursor_mock

        truncate_tables()
        self.assertTrue(cursor_mock.execute.called)
        expected_sql = "TRUNCATE myapp_userprofile,myapp_companyprofile RESTART IDENTITY CASCADE;"
        cursor_mock.execute.assert_called_once_with(expected_sql)
