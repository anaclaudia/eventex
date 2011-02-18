from django.conf.urls.defaults import *
#from core.views import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',    
    (r'^$', 'direct_to_template',{'template':'index.html'}),
    (r'^subscription/', include('subscription.urls', namespace='subscription')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns ('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT}),
    )
