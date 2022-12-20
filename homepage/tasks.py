from celery import shared_task
from django.conf import settings
from django.core.mail import send_mass_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives


User = get_user_model()


@shared_task
def send_mail_task():
    my_url  = 'https://shopatpurchased.com'
    subject = 'Visit your profile'
    message =  'Hey there, do you have a product to sell\n then follow this steps\n 1) Register and sign in \n 2) goto your profile \n 3) click on creat post \n' + my_url
    email_from = settings.EMAIL_HOST_USER
    recipient_ = list(User.objects.values_list('email',flat=True))
    msg = EmailMultiAlternatives(subject, message, email_from,  bcc=recipient_)
    msg.send()
    return "Mail has been sent........"




# https://episyche.com/blog/how-to-run-periodic-tasks-in-django-using-celery