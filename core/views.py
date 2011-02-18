from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request, template=None):
    return render_to_response(template, RequestContext(request))

