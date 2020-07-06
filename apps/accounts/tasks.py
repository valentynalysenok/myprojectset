from celery import shared_task
from celery.worker import request

from django.core.mail import EmailMessage

from django.template.loader import render_to_string

from apps.accounts.models import User


@shared_task
def send_verification_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'MyProjectSet email verification'

    message = render_to_string('accounts/activate_account.html', {
        'email': user.email,
        'domain': 'lysenok.planeks.net',
        'id': user.id,
    })
    email = EmailMessage(subject=subject,
                         body=message,
                         from_email='valentynalysenok@planeks.net',
                         to=[user.email])
    email.send()
