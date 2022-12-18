from celery import shared_task
from django.conf import settings
from django.core.mail import send_mass_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def send_mail_task():
    my_url  = 'https://shopatpurchased.com'
    subject = 'Amazing Ember Offers'
    message = 'BUSINESS DEALS FOR EVERY LASU STUDENT \n BUY AND SELL AT EASE , Huray !!! \n' + my_url
    email_from = settings.EMAIL_HOST_USER
    recipient_list = list(User.objects.values_list('email',flat=True))
    mytupple =( subject, message, email_from, recipient_list )
    send_mass_mail(mytupple, fail_silently= False)
    return "Mail has been sent........"