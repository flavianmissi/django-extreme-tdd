from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^p/', include('example_project.posts.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
