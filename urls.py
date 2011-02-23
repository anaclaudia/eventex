from django.conf.urls.defaults import *
<<<<<<< HEAD
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
=======


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.homepage', name='homepage'),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
    )
>>>>>>> aula-2
