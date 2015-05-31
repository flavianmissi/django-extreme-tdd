from django.conf.urls import url
from .views import PostDetails


urlpatterns = [
    # Examples:
    # url(r'^$', 'example_project.views.home', name='home'),

    url(r'^(?P<pk>[0-9]+)/$', PostDetails.as_view(), name="posts"),
]
