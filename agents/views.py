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
@api_view(['GET'])
def agent_list(request):
    if request.method == 'GET':
        agents_ = Agent.objects.all()
        serializer = AgentSerializer(agents_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def distributor_agent_list(request):
    """ get agents per product
        through agents, distributor association
    """
    if request.method == 'GET':
        cursor = connection.cursor()
        prod_agents = []
        pk = request.user.id

        # TODO: agents per product ID

        try:
            # cursor.execute("SELECT agent_id FROM agents_agent_products WHERE product_id = %s", [pk])
            cursor.execute("""select a.name, a.phone_number, a.id, p.name as product_name from products_product
                                as p join agents_agent_products as m on
                                p.id = m.product_id join agents_agent as a on
                                m.agent_id = a.id where p.owner_id = %s""", [pk])

            __agents_object = dict_fetch_all(cursor=cursor)
            print __agents_object

        except Agent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            cursor.close()

        # no agents associated with product
        if len(__agents_object) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if isinstance(__agents_object, types.ListType):
            for agent_ in __agents_object:
                prod_agents.append(agent_)

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
