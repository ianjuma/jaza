from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products_ = Product.objects.all()
        serializer = ProductSerializer(products_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def distributor_products(request):
    if request.method == 'GET':
        product = Product.objects.filter(owner_id=request.user)
        serializer = ProductSerializer(product, many=True)

        for data in serializer.data:
            dt = data['created_at']
            data['created_at'] = dt.split('T')[0]

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
