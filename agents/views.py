from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from agents.models import Agent
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
@api_view(['GET', 'POST'])
def agent_list(request):
    if request.method == 'GET':
        agents_ = Agent.objects.all()
        serializer = AgentSerializer(agents_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = AgentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def distributor_agent_list(request, pk):
    """ get agent's per product
    agents , distributor association
    """
    if request.method == 'GET':
        cursor = connection.cursor()
        # get dist from user.id -> products -> per product
        # my agents per product - get products by owner
        # get agents for products
        prod_agents = []

        try:
            cursor.execute("SELECT agent_id FROM agents_agent_products WHERE product_id = %s", [pk])
            __agents_object = dict_fetch_all(cursor=cursor)
            __agents_ids = []
            for obj in __agents_object:
                keys, values = obj.keys(), obj.values()
                __agents_ids.append(values[0])

        except Agent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            cursor.close()

        # no agents associated with product
        if len(__agents_ids) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if len(__agents_ids) == 1:
            agent = Agent.objects.get(pk=__agents_ids[0])
            agent = AgentSerializer(agent)

            return Response(agent.data, status=status.HTTP_200_OK)
        elif isinstance(__agents_ids, types.ListType):
            for agent_id in __agents_ids:
                agent = Agent.objects.get(pk=agent_id)
                agent_ = AgentSerializer(agent)
                prod_agents.append(agent_.data)

        # agents_ = dict_fetch_all(cursor=cursor)
        # object created had - { agent info, product name, }
        # create object with product name - constant for query X, agent info
        # get agent_id
        # agent_ids = dict_fetch_all(cursor=cursor)
        # get agents info - pagination? - get agent info -> pagination

        return Response(prod_agents, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'PUT', 'DELETE'])
def agent_detail(request, pk):
    try:
        agent = Agent.objects.get(pk=pk)
    except Agent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgentSerializer(agent, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AgentSerializer(agent, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TODO: permission classes, and auth