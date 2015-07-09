import urllib
import urllib2
import json

from django.conf import settings


class CrunchGatewayException(Exception):
    pass


class CrunchGateway:

    def __init__(self):
        self.CrunchInterface = settings.CRUNCH_INTERFACE

    def get_airtime_stats(self, metric, start_date, end_date,
                          agent_id, product_id, category='sent',
                          granularity='day'):

        values = {
            'agentId': agent_id,
            'productId': product_id,
            'metric': metric,
            'granularity': granularity,
            'startDate': start_date,
            'endDate': end_date,
        }

        headers = {
            'Accept': 'application/json',
            'api-key': settings.API_KEY
        }

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
