from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

User=get_user_model()

@periodic_task(
run_every=(crontab(hour=12, minute=50)), #runs exactly at 3:34am every day
name="Dispatch_scheduled_mail",
reject_on_worker_lost=True,
ignore_result=True)
def schedule_mail():
    message = render_to_string('mailTemplate/schedule_mail.html')
    mail_subject = 'Top Offers on ShopatPurchased'
    to_email = list(User.objects.values_list('email',flat=True))
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
