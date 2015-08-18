from rest_framework import views, permissions
from rest_framework.response import Response

from utils.crunchGateway import CrunchGateway, CrunchGatewayException
from utils.sleuthGateway import SleuthGateway, SleuthGatewayException


class CrunchAgentStatsView(views.APIView):
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
            response_data = gateway.get_agent_stats(
                category=category,
                agent_id=agent_id,
                product_id=product_id,
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


class CrunchProductStatsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = request.query_params
        try:
            category = data['category']
            product_id = data['productId']
            start_date = data['startDate']
            end_date = data['endDate']
            granularity = data['granularity']
            metric = data['metric']

            gateway = CrunchGateway()
            response_data = gateway.get_product_stats(
                category=category,
                product_id=product_id,
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


class SleuthUserTopUpView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        data = request.query_params
        try:
            category = data['userCategory']
            currency_code = data['currencyCode']
            user_id = data['userId']
            source = data['source']
            amount = data['amount']
            ref_id = data['refId']

            gateway = SleuthGateway()
            response_data = gateway.top_up_user(
                user_category=category,
                user_id=user_id,
                source=source,
                amount=amount,
                ref_id=ref_id,
                currency_code=currency_code
            )
            print response_data

        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        return Response(response_data)


class SleuthGetUserBalanceView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = request.query_params
        try:
            user_category = data['userCategory']
            user_id = data['userId']

            gateway = SleuthGateway()
            response_data = gateway.get_user_balance(
                user_category=user_category,
                user_id=user_id,
            )

        except SleuthGatewayException, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        except Exception, e:
            print "Caught exception when calling AT Gateway: " + str(e)
            response_data = {}

        return Response(response_data)
