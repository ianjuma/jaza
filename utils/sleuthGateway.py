import urllib
import urllib2
import json

from django.conf import settings


class SleuthGatewayException(Exception):
    pass


class SleuthGateway:

    def __init__(self):
        self.SleuthInterface = settings.SLEUTH_INTERFACE

    def top_up_agent(self, user_id, agent_id, product_id, amount):
        values = {
            'userId': user_id,
            'agentId': agent_id,
            'productId': product_id,
            'amount': amount
        }

        headers = {'Accept': 'application/json'}

        try:
            url = '%s/user-data/billing' % self.SleuthInterface
            data = urllib.urlencode(values)
            request = urllib2.Request(url, data, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise SleuthGatewayException(the_page)

        else:
            decoded = json.loads(the_page)
            if decoded['status']:
                return decoded['responses']
            else:
                raise SleuthGatewayException(decoded['errorMessage'])

    def get_agent_balance(self, agent_id, product_id):
        values = {
            'agentId': agent_id,
            'productId': product_id,
        }

        headers = {'Accept': 'application/json'}

        try:
            url = '%s/billing/user-balance' % self.SleuthInterface
            data = urllib.urlencode(values)
            request = urllib2.Request(url, data, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise SleuthGatewayException(the_page)

        else:
            decoded = json.loads(the_page)

            if decoded['status']:
                return {
                    'currencyCode': decoded['currencyCode'],
                    'amount': decoded['amount']
                }
            else:
                raise SleuthGatewayException('Error while fetching balance')
