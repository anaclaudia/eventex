from django.shortcuts import render_to_response
<<<<<<< HEAD
from django.template import RequestContext

#def homepage(request):
#    return render_to_response('index.html', RequestContext(request))
=======


def homepage(request):
    from django.conf import settings
    context = {'MEDIA_URL': settings.MEDIA_URL}

    return render_to_response('index.html', context)
>>>>>>> aula-2
