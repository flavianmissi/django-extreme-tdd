from unittest import TestCase
from mock import patch, Mock, MagicMock
from extreme.cleanup import _collect_apps, _collect_model_tables, truncate_tables


class CleanUpTests(TestCase):

    @patch("extreme.cleanup.get_app", new=lambda x: x)
    @patch("extreme.cleanup.settings")
    def test_should_collect_apps_from_LOCAL_APPS(self, settings_mock):
        settings_mock.LOCAL_APPS = ["profiles", "tags", "articles"]
        apps = _collect_apps()
        expected_apps = settings_mock.LOCAL_APPS
        self.assertListEqual(expected_apps, apps)

    @patch("extreme.cleanup.get_models")
    def test_should_collect_models_from_app(self, get_models_mock):
        models_mock = [
            Mock(_meta=Mock(db_table="myapp_userprofile")),
            Mock(_meta=Mock(db_table="myapp_companyprofile")),
        ]
        get_models_mock.return_value = models_mock

        models = _collect_model_tables(app="some_mock_app")
        expected = ["myapp_userprofile", "myapp_companyprofile"]
        self.assertListEqual(expected, models)

    @patch("extreme.cleanup.connections")
    @patch("extreme.cleanup._collect_model_tables")
    @patch("extreme.cleanup._collect_apps")
    def test_truncate_tables(self, apps_mock, tables_mock, connections_mock):
        apps_mock.return_value = ["myapp"]
        tables_mock.return_value = ["myapp_userprofile", "myapp_companyprofile"]
        cursor_mock = MagicMock()
        connections_mock.__getitem__.return_value.cursor.return_value = cursor_mock

        truncate_tables()
        self.assertTrue(cursor_mock.execute.called)
        expected_sql = "TRUNCATE myapp_userprofile,myapp_companyprofile RESTART IDENTITY CASCADE;"
        cursor_mock.execute.assert_called_once_with(expected_sql)
