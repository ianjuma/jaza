from django.conf import settings

from rest_framework import status, views, permissions
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from utils.africasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from utils.sleuthGateway import SleuthGateway, SleuthGatewayException
from utils.crunchGateway import CrunchGateway, CrunchGatewayException


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    def post(self, request, format=None):
        username = request.user.username
        file_obj = request.data['file']
        filename = '%s:%s' % (username, file_obj.name)
        try:
            with open('/var/tmp/data/cowbell/' + filename, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

        except Exception, ex:
            return Response({
                'status': 'Failed',
                'error': 'Error while saving file'
            }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                'status': 'Success',
                'filename': filename
            })


class NumQueuedCallsView(views.APIView):
    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    def get(self, request, format=None):
        try:
            data = request.query_params
            phoneNumbers = data['phoneNumbers']
            username = settings.API_USER['username']
            apikey = settings.API_USER['api_key']

            gateway = AfricasTalkingGateway(username, apikey)

            entries = gateway.getNumQueuedCalls(phoneNumbers)
            responseData = {'entries': entries}

        except AfricasTalkingGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {'numQueuedCalls': 0}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {'numQueuedCalls': 0}

        return Response(responseData)


class SleuthView(views.APIView):
    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    def get(self, request, format=None):
        data = request.query_params
        query = data['query']
        if query == 'callSessionUserData':
            return self.getCallSessionUserData(data)
        elif query == 'balance':
            return self.getBalance(request.user)
        elif query == 'billingUserData':
            return self.getBillingUserData(data, request.user)
        else:
            return Response({
                'error': 'Invalid query: %s' % query
            }, status=status.HTTP_400_BAD_REQUEST)

    def getBillingUserData(self, data, user):
        try:
            userId = user.id
            pageNumber = data['pageNumber']
            count = data['count']

            gateway = SleuthGateway()
            responseData = gateway.getBillingUserData(
                userId=userId,
                pageNumber=pageNumber,
                count=count
            )

        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        return Response(responseData)

    def getBalance(self, user):
        try:
            userId = user.id

            gateway = SleuthGateway()
            responseData = gateway.getBalance(
                userId=userId
            )

        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        return Response(responseData)

    def getCallSessionUserData(self, data):
        try:
            sessionMode = data['sessionMode']
            handlerId = data['handlerId']
            pageNumber = data['pageNumber']
            count = data['count']
            startDate = data[
                'startDate'] if 'startDate' in data else None
            endDate = data['endDate'] if 'endDate' in data else None
            callerNumber = data[
                'callerNumber'] if 'callerNumber' in data else None
            destinationNumber = data[
                'destinationNumber'] if 'destinationNumber' in data else None
            direction = data[
                'direction'] if 'direction' in data else None

            gateway = SleuthGateway()
            responseData = gateway.getCallSessionUserData(
                sessionMode=sessionMode,
                handlerId=handlerId,
                pageNumber=pageNumber,
                count=count,
                startDate=startDate,
                endDate=endDate,
                callerNumber=callerNumber,
                destinationNumber=destinationNumber,
                direction=direction
            )

        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        return Response(responseData)


class CrunchView(views.APIView):
    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    def get(self, request, format=None):
        data = request.query_params
        try:
            username = request.user.username
            category = data['category']
            startDate = data['startDate']
            endDate = data['endDate']
            metric = data['metric']
            gateway = CrunchGateway()
            responseData = gateway.getStats(
                username=username,
                category=category,
                startDate=startDate,
                endDate=endDate,
                metric=metric
            )

        except CrunchGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            responseData = {}

        return Response(responseData)
