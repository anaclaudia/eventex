import datetime
from django.contrib import admin
from django.utils.translation import ugettext as _
from subscription.models import Subscription

<<<<<<< HEAD
class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name','email',	'phone', 'created_at', 'subscribed_today')
	date_hierarchy = 'created_at'
	search_fields = ('name', 'cpf','email','phone', 'created_at')
	list_filter = ['created_at']
	
	def subscribed_today(self,obj):
		return obj.created_at.date() == datetime.date.today()
		
	subscribed_today.short_description = _('Inscrito hoje?')
	subscribed_today.boolean = True
	
=======

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()
    subscribed_today.short_description = _('Inscrito hoje?')
    subscribed_today.boolean = True

>>>>>>> aula-2
admin.site.register(Subscription, SubscriptionAdmin)
