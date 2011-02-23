from django import forms
from subscription.models import Subscription

<<<<<<< HEAD
class SubscriptionForm(forms.ModelForm):
	class Meta:
	model = Subscription
	exclude = ('created_at',)
=======

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('created_at',)
>>>>>>> aula-2
