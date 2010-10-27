#-*- coding: utf-8 -*-
from django.db import models
from subscription.receivers import send_subscription_email

class Subscription(models.Model):
    """
    # Importa o model Subscription
    >>> from subscription.models import Subscription


    # Faz uma inscrição bem sucedida
    >>> Subscription.objects.create(name='Henrique Bastos', cpf='05633165780', email='henrique@bastos.net', phone='21-9618-6180')
    <Subscription: ...


    # CPF deve ser único
    >>> Subscription.objects.create(name='Henrique Bastos', cpf='05633165780', email='othermail@bastos.net', phone='21-9618-6180')
    Traceback (most recent call last):
    ...
    IntegrityError: column cpf is not unique


    # Email deve ser único
    >>> Subscription.objects.create(name='Henrique Bastos', cpf='38067528772', email='henrique@bastos.net', phone='21-9618-6180')
    Traceback (most recent call last):
    ...
    IntegrityError: column email is not unique

    """
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s - %s' % (self.pk, self.name, self.email)

models.signals.post_save.connect(send_subscription_email, sender=Subscription)
