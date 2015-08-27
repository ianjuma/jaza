from rest_framework import views, permissions
from rest_framework.response import Response

from utils.crunchGateway import CrunchGateway, CrunchGatewayException
from utils.sleuthGateway import SleuthGateway, SleuthGatewayException
from datetime import datetime, timedelta


class CrunchAgentStatsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        # data = request.query_params
        try:
            agent_id = pk
            """
            agent_id = data['agentId']
            category = data['category']
            product_id = data['productId']
            start_date = data['startDate']
            end_date = data['endDate']
            granularity = data['granularity']
            metric = data['metric']
            """
            now = datetime.now()
            time_deficit = timedelta(days=1)
            # stats for last 7 days
            back_date = now - time_deficit
            back_date = back_date.strftime("%Y-%m-%d")

            gateway = CrunchGateway()
            response_data = gateway.get_agent_stats(
                category='sent',
                agent_id=agent_id,
                start_date=back_date,
                end_date=now.strftime("%Y-%m-%d"),
                granularity='day',
                metric='cost'
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

    def get(self, request, pk, format=None):
        # data = request.query_params
        try:
            product_id = pk
            now = datetime.now()
            time_deficit = timedelta(days=2)
            # stats for last 7 days
            back_date = now - time_deficit
            """
            product_id = data['productId']
            category = data['category']
            start_date = data['startDate']
            end_date = data['endDate']
            granularity = data['granularity']
            metric = data['metric']
            """

            gateway = CrunchGateway()
            response_data = gateway.get_product_stats(
                category='sent',
                product_id=product_id,
                start_date=back_date.strftime("%Y-%m-%d"),
                end_date=now.strftime("%Y-%m-%d"),
                granularity='day',
                metric='cost'
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
        data = request.data
        try:
            category = 'Agent'
            currency_code = 'KES'
            user_id = data['agentID']
            source = data['source']
            amount = data['amount']
            ref_id = data['refID']
            print ref_id, amount, source, user_id, currency_code, category

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
