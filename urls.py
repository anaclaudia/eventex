from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
	(r'^$', 'direct_to_template', {'template':'index.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^subscription/', include('subscription.urls', namespace='subscription')),
    
)

if settings.DEBUG:
    urlpatterns += patterns ('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT}),)
