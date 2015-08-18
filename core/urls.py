from .views import index, logout, refresh_starred_segments
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^refresh_segments/$', refresh_starred_segments),
    url(r'^logout/$', logout),
)
