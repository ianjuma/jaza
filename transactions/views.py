from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


@api_view(['GET', 'POST'])
def transaction_list(request):
    if request.method == 'GET':
        distributors_ = Transaction.objects.all()
        serializer = TransactionSerializer(distributors_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def transaction_detail(request, pk):
    try:
        product = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TransactionSerializer(product, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)