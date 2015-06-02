from rest_framework.response import Response
from rest_framework import permissions, viewsets, views, status
from rest_framework.decorators import api_view

from distributors.models import Distributor
from distributors.permissions import IsRealDistributor
from distributors.serializers import DistributorSerializer


class DistributorApi(views.APIView):
    # authentication_classes = (auth)
    permission_classes = permissions.IsAuthenticated

    @staticmethod
    def get(self, request):
        distributors = [distributor.name for distributor in Distributor.objects.all()]
        return Response(distributors)


class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.order_by('-created_at')
    serializer_class = Distributor

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.AllowAny()
        return permissions.IsAuthenticated(), IsRealDistributor()

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(DistributorViewSet, self).perform_create(serializer)


class AccountDistributorsViewSet(viewsets.ViewSet):
    queryset = Distributor.objects.select_related('author').all()
    serializer_class = DistributorSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def distributors(request):
    if request.method == 'GET':
        distributors_ = Distributor.objects.all()
        serializer = DistributorSerializer(distributors_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = DistributorSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def distributor_detail(request, pk):
    try:
        distributor = Distributor.objects.get(pk=pk)
    except distributor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DistributorSerializer(distributor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = DistributorSerializer(distributor, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        distributor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)