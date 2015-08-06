from rest_framework import views, permissions
from rest_framework.response import Response

from utils.crunchGateway import CrunchGateway, CrunchGatewayException
from utils.sleuthGateway import SleuthGateway, SleuthGatewayException


class CrunchView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = request.query_params
        try:
            category = data['category']
            product_id = data['productId']
            agent_id = data['agentId']
            start_date = data['startDate']
            end_date = data['endDate']
            granularity = data['granularity']
            metric = data['metric']

            gateway = CrunchGateway()
            response_data = gateway.get_airtime_stats(
                category=category,
                product_id=product_id,
                agent_id=agent_id,
                start_date=start_date,
                end_date=end_date,
                granularity=granularity,
                metric=metric
            )

        except CrunchGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        return Response(response_data)


class SleuthAgentTopUpView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = request.query_params
        try:
            agent_id = data['agentId']
            product_id = data['productId']
            user_id = data['userId']
            amount = data['amount']

            gateway = SleuthGateway()
            response_data = gateway.top_up_agent(
                agent_id=agent_id,
                product_id=product_id,
                user_id=user_id,
                amount=amount
            )
        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        return response_data


class SleuthGetAgentBalanceView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = request.query_params
        try:
            product_id = data['productId']
            agent_id = data['agentId']

            gateway = SleuthGateway()
            response_data = gateway.get_agent_balance(
                product_id=product_id,
                agent_id=agent_id,
            )

        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        return Response(response_data)
