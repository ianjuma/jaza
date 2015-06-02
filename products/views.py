from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view

from products.models import Product
from products.permissions import IsAuthorOfPost
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = Product

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.AllowAny()
        return permissions.IsAuthenticated(), IsAuthorOfPost()

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(ProductViewSet, self).perform_create(serializer)


class AccountProductsViewSet(viewsets.ViewSet):
    queryset = Product.objects.select_related('author').all()
    serializer_class = ProductSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        distributors_ = Product.objects.all()
        serializer = ProductSerializer(distributors_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)