from __future__ import absolute_import, unicode_literals
from app.celery import app
import time
from celery import shared_task


@shared_task
def debug_task(self):
    """Check Celery is working by just printing out the task context"""
    print('Request: Inside task - {0!r}'.format(self.request))


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 5)
    return True