from django.conf.urls.defaults import *

<<<<<<< HEAD
urlpatterns = patterns('subscription.views',
	url(r'^$', 'subscribe', name='subscribe'),
	url(r'^(\d+)/sucesso/$', 'success', name='success'),
=======

urlpatterns = patterns('subscription.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
>>>>>>> aula-2
)
