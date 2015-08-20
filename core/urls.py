from .views import index, logout, refresh_starred_segments, refresh_segment_efforts, segment
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^refresh_segments/$', refresh_starred_segments),
    url(r'^segment/(?P<segment_id>\d+)$', segment),
    url(r'^segment/(?P<segment_id>\d+)/refresh_efforts$', refresh_segment_efforts),
    url(r'^logout/$', logout),
)
