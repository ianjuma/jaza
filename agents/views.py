from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from agents.models import Agent
from products.models import Product
from agents.serializers import AgentSerializer

from django.db import connection
import types


def dict_fetch_all(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def agent_list(request):
    if request.method == 'GET':
        agents_ = Agent.objects.all()
        serializer = AgentSerializer(agents_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def distributor_agent_list(request, pk=None):
    """ get agents per product
        get agents from the products, agents association
        through agents, distributor association
    """
    if request.method == 'GET':
        cursor = connection.cursor()
        prod_agents = []
        pk = pk

        # TODO: agents per product ID

        try:
            cursor.execute("SELECT agent_id FROM agents_agent_products WHERE product_id = %s", [pk])

            __agents_object = dict_fetch_all(cursor=cursor)
            print __agents_object

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            cursor.close()

        # no agents associated with product
        if len(__agents_object) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if isinstance(__agents_object, types.ListType):
            for agent_ in __agents_object:
                try:
                    agent_info = Agent.objects.get(pk=agent_['agent_id'])
                    agent_detail_ = AgentSerializer(agent_info)
                    prod_agents.append(agent_detail_.data)
                except Product.DoesNotExist:
                    pass

        return Response(prod_agents, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def agent_detail(request, pk):
    try:
        agent = Agent.objects.get(pk=pk)
    except Agent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgentSerializer(agent, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
