from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
#    url(r'^prueba/', include('basica.prueba.urls')),
#)


urlpatterns = patterns('',
    url(r'^prueba/$', 'prueba.views.index'),
    url(r'^prueba/(?P<poll_id>\d+)/$', 'prueba.views.detail'),
    url(r'^prueba/(?P<poll_id>\d+)/results/$', 'prueba.views.results'),
    url(r'^prueba/(?P<poll_id>\d+)/vote/$', 'prueba.views.vote')
)