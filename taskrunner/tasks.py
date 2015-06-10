from __future__ import absolute_import

from celery import shared_task


@shared_task
def send_airtime(amount, recipient):
    print amount, recipient


@shared_task
def send_sms():
    pass


@shared_task
def send_forgot_pin_sms():
    pass