import logging
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import User

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'Welcome to Our Platform!'
    message = f'Hello {user.name},\n\nWelcome to our platform! We are glad to have you.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    try:
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Welcome email sent to user {user.email}")
    except Exception as e:
        logger.error(f"Error sending welcome email to user {user.email}: {str(e)}")
