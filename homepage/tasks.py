from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


User = get_user_model()


@shared_task
def send_mail_task():
    my_url  = 'https://shopatpurchased.com'
    subject = 'shopatpurchased team'
    message =  render_to_string('mail.html', {'context': my_url})
    email_from = settings.EMAIL_HOST_USER
    recipient_ =['ayoajetunmobi78@gmail.com',]
    # recipient_ = list(User.objects.values_list('email',flat=True))
    msg = EmailMultiAlternatives(subject, message, email_from,  bcc=recipient_)
    msg.attach_alternative(message,'text/html')
    msg.send()
    return "Mail has been sent........"




# https://episyche.com/blog/how-to-run-periodic-tasks-in-django-using-celery