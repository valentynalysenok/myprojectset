from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task
def send_verification_email(user, domain):
    subject = 'MyProjectSet email verification'
    message = render_to_string('accounts/activate_account.html', {
        'user': user,
        'domain': domain,
        'id': user.id,
    })
    email = EmailMessage(subject=subject,
                         body=message,
                         from_email='valentynalysenok@planeks.net',
                         to=[user.email])
    email.send()
