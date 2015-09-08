from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from distributors.serializers import DistributorSerializer
from django.contrib.auth.models import User


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def distributor_list(request):
    if request.method == 'GET':
        distributors_ = User.objects.all()
        serializer = DistributorSerializer(distributors_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = DistributorSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'PUT', 'DELETE'])
def distributor_detail(request, pk):
    try:
        distributor = User.objects.get(pk=pk)
    except User.DoesNotExist:
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