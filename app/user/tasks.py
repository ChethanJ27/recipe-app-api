from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from .utils import sendVerificationMail
from .models import UserModel
import logging


logger = logging.getLogger("user_tasks")

@shared_task
def debug_task(self):
    """Check Celery is working by just printing out the task context"""
    print('Request: Inside task - {0!r}'.format(self.request))


@shared_task
def send_verification_mail(username,email):
    """sending verification email logic will come here"""
    sendVerificationMail(username=username,email=email)
    return True

@shared_task
def cleanup_deleted_users():
    try:
       res = UserModel.objects.filter(is_deleted=True).delete()
       logger.info(res)
    except Exception as e:
        logger.error(e)