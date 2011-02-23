from django.core.urlresolvers import reverse
<<<<<<< HEAD
from django.http import HttpResponseRedirect, HttpResponse
from django shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from subscription.forms import SubscriptionForm
from subscription.models import Subscription

def new(request):
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html', context)

def create(request):
	form = SubscriptionForm(request.POST)
	
	if not form.is_valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subscription/new.html', context)
	
	subscription = form.save()
#	send_mail_confirmation(subscription)
	return HttpResponseRedirect(reverse('subscription:success', args=[subscription.pk]))

def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def success(request, pk):
	subscription = get_object_or_404(Subscription, pk=pk)
	context = RequestContext(request,{'subscription': subscription})
	return render_to_response('subscription/success.html', context)

#def send_mail_confirmation(subscription):
#	from django.core.email import send_email
#	send_email(
#		subject=u'Inscrição no eventex', 
#		message=u'Obrigado por se inscrever!!', 
#		from_email='contato@eventex.com.br', 
#		recipient_list=[subscription.email],
#	)
=======
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from subscription.utils import send_subscription_email


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()
    # notifica o cadastro
    send_subscription_email(subscription)
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
>>>>>>> aula-2
