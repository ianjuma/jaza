from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from agents.models import Agent
from agents.serializers import AgentSerializer
# from agents.permissions import IsRealAgent


# TODO: permission classes, and auth
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


@api_view(['GET', 'PUT', 'DELETE'])
def agent_detail(request, pk):
    try:
        agent = Agent.objects.get(phone_number=pk)
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
