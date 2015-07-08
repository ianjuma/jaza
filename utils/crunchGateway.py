import urllib
import urllib2
import json

from django.conf import settings


class CrunchGatewayException(Exception):
    pass


class CrunchGateway:

    def __init__(self):
        self.CrunchInterface = settings.CRUNCH_INTERFACE

    def getStats(self,
                 username,
                 category,
                 startDate,
                 endDate,
                 metric):

        values = {
            'username': username,
            'metric': metric,
            'granularity': 'day',
            'startDate': startDate,
            'endDate': endDate
        }

        headers = {'Accept': 'application/json'}

        try:
            url = '%s/%s?%s' % (self.CrunchInterface,
                                category,
                                urllib.urlencode(values))
            print 'Sending request to ' + url
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            the_page = response.read()

        except urllib2.HTTPError as e:
            the_page = e.read()
            raise CrunchGatewayException(the_page)

        else:
            decoded = json.loads(the_page)
            return decoded['responses']
