import urllib
import urllib2
import json

from django.conf import settings


class SleuthGatewayException(Exception):
    pass


class SleuthGateway:

    def __init__(self):
        self.SleuthInterface = settings.SLEUTH_INTERFACE

    def getCallSessionUserData(
        self,
        sessionMode,
        handlerId,
        pageNumber,
        count,
        startDate,
        endDate,
        callerNumber,
        destinationNumber,
        direction
    ):
        values = {
            'sessionMode': sessionMode,
            'handlerId': handlerId,
            'pageNumber': pageNumber,
            'count': count
        }
        if startDate:
            values['startDate'] = startDate
        if endDate:
            values['endDate'] = endDate
        if callerNumber:
            values['callerNumber'] = callerNumber
        if destinationNumber:
            values['destinationNumber'] = destinationNumber
        if direction:
            values['direction'] = direction

        headers = {'Accept': 'application/json'}

        try:
            url = '%s/user-data/call-session' % self.SleuthInterface
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

    def getBillingUserData(
        self,
        userId,
        pageNumber,
        count
    ):
        values = {
            'userId': userId,
            'pageNumber': pageNumber,
            'count': count
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

    def getBalance(
        self,
        userId
    ):
        values = {
            'userId': userId,
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
