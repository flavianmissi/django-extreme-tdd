"""
Testing cleanup helpers.
These cleanup functions assume the user uses a separate settings list for local
applications under the name of LOCAL_APPS.
"""
from django.db import connections
from django.db.models import get_app, get_models
from django.conf import settings


def truncate_tables():
    apps = _collect_apps()

    tables = []
    for app in apps:
        tables.extend(_collect_model_tables(app))

    # PostgreSQL only - for now
    sql = "TRUNCATE {} RESTART IDENTITY CASCADE;".format(",".join(tables))
    cursor = connections["default"].cursor()
    cursor.execute(sql)


def _collect_apps():
    return [get_app(app_name.split(".")[-1]) for app_name in settings.LOCAL_APPS]


def _collect_model_tables(app):
    return [model._meta.db_table for model in get_models(app)]
