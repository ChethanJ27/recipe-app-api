from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.core.mail import send_mail


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def add_token_to_blackList(refresh_token):
    token = RefreshToken(refresh_token)
    token.blacklist()

def sendVerificationMail(username,email):
    subject = 'welcome to GFG world'
    message = f'Hi {username}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, message, email_from, recipient_list )
