from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from products.models import Distributor
from distributors.serializers import DistributorSerializer


@api_view(['GET', 'POST'])
def distributor_list(request):
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
        # user = User.objects.get(pk=pk)
        distributor = Distributor.objects.get(pk=pk)
    except Distributor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DistributorSerializer(distributor)
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