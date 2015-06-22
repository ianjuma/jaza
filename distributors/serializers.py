from rest_framework import serializers

from products.models import Account, Product
from products.serializers import ProductSerializer


# TODO: fetch distributor products - set many=True
class DistributorSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=False, required=False, many=True)

    class Meta:
        model = Account

        # 'created_at', 'updated_at'
        fields = ('id', 'email', 'products', 'username', 'last_name', 'first_name',)
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(DistributorSerializer, self).get_validation_exlusions()

            return exclusions + ['id', 'user']

    def create(self, validated_data):
        products = validated_data.pop('products', None)

        distributor = Account.objects.create(**validated_data)
        for product in products:
            prod = Product.objects.create()

            prod.name = product.get('name')
            prod.category = product.get('category')
            prod.owner = product.get('owner')
            print prod.name

            prod.save()
            distributor.products.add(prod)

        distributor.save()
        return distributor

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)

        instance.username = validated_data.get('username', None)
        instance.email = validated_data.get('email', None)
        instance.last_name = validated_data.get('last_name', None)
        instance.first_name = validated_data.get('first_name', None)
        instance.save()

        # delete products not included in the update
        product_ids = [product['id'] for product in validated_data['products']]
        for product in products:
            if product.id not in product_ids:
                product.delete()

        distributor = Account.objects.create(**validated_data)

        # create or update page instances
        for product in validated_data['products']:
            product = Product(id=product['id'], name=product['name'],
                              category=product['category'], owner=product['owner'], product=instance)
            product.save()

        for product in products:
            prod = Product.objects.create()

            prod.name = product.get('name')
            prod.category = product.get('category')
            prod.owner = product.get('owner')

            prod.save()
            distributor.products.add(prod)

        distributor.save()
        return distributor