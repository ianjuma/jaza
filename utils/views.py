from rest_framework import views, permissions
from rest_framework.response import Response

from utils.crunchGateway import CrunchGateway, CrunchGatewayException
from utils.sleuthGateway import SleuthGateway, SleuthGatewayException

from datetime import datetime, timedelta


class CrunchAgentStatsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = request.query_params
        try:
            agent_id = data.get('agentId', None)
            start_date = data.get('startDate', None)
            end_date = data.get('endDate', None)
            category = data.get('category', None)

            if start_date is None and end_date is None:
                end_date = datetime.now().strftime("%Y-%m-%d")
                start_date = datetime.now() - timedelta(days=7)
                start_date = start_date.strftime("%Y-%m-%d")

                start_date = start_date.split('T')[0]
                end_date = end_date.split('T')[0]
            else:
                first_ = end_date.split('/')[0]
                second_ = end_date.split('/')[1]
                third_ = end_date.split('/')[2]
                end_date = third_ + '-' + second_ + '-' + first_

                first_ = start_date.split('/')[0]
                second_ = start_date.split('/')[1]
                third_ = start_date.split('/')[2]
                start_date = third_ + '-' + second_ + '-' + first_

            if category is None:
                category = 'sent'

            print start_date, end_date, category

            gateway = CrunchGateway()
            response_data = gateway.get_agent_stats(
                category=category,
                agent_id=agent_id,
                start_date=start_date,
                end_date=end_date,
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

    def get(self, request, format=None):
        data = request.query_params
        try:
            product_id = data.get('productId', None)
            category = data.get('category', None)
            start_date = data.get('startDate', None)
            end_date = data.get('endDate', None)

            if end_date is not None and start_date is not None:
                first_ = end_date.split('/')[0]
                second_ = end_date.split('/')[1]
                third_ = end_date.split('/')[2]
                end_date = third_ + '-' + second_ + '-' + first_

                first_ = start_date.split('/')[0]
                second_ = start_date.split('/')[1]
                third_ = start_date.split('/')[2]
                start_date = third_ + '-' + second_ + '-' + first_

            if start_date is None and end_date is None:
                end_date = datetime.now().strftime("%Y-%m-%d")
                start_date = datetime.now() - timedelta(days=7)
                start_date = start_date.strftime("%Y-%m-%d")

                start_date = start_date.split('T')[0]
                end_date = end_date.split('T')[0]

            if category is None:
                category = 'sent'

            gateway = CrunchGateway()
            response_data = gateway.get_product_stats(
                category=category,
                product_id=product_id,
                start_date=start_date,
                end_date=end_date,
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
