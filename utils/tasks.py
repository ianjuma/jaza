from __future__ import absolute_import

from celery import shared_task
from taskrunner.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

api = AfricasTalkingGateway(
    username_='settings.username', apiKey_='settings.api_key')


@shared_task
def send_airtime(amount, recipient):
    try:
        api.sendAirtime([{amount, recipient}])
    except AfricasTalkingGatewayException:
        pass


@shared_task
def send_sms(to, _from):
    api.sendMessage(to_=to, message_="", from_=_from, retryDurationInHours_=1)
    pass


@shared_task
def send_forgot_pin_sms(to, _from):
    api.sendMessage(to_=to, message_="", from_=_from)
    pass
