from .views import index, logout
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^logout/$', logout),
)
