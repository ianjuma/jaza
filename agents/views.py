from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view

from agents.models import Agent
from agents.permissions import IsRealAgent
from agents.serializers import AgentSerializer


@api_view(['GET', 'POST'])
def agent_list(request):
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializers = AgentSerializer(agents, many=True)
        return Response(serializers, status=status.HTTP_200_OK)
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
        agent = Agent.objects.get(pk=pk)
    except agent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgentSerializer(agent, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AgentSerializer(agent, request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.order_by('-created_at')
    serializer_class = AgentSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.AllowAny()
        return permissions.IsAuthenticated(), IsRealAgent()

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(AgentViewSet, self).perform_create(serializer)


class AccountAgentsViewSet(viewsets.ViewSet):
    queryset = Agent.objects.select_related('author').all()
    serializer_class = AgentSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
