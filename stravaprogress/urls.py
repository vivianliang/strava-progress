from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stravaprogress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('', include('core.urls')),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
