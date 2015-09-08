from rest_framework import serializers

from products.models import Product
from django.contrib.auth.models import User
from products.serializers import ProductSerializer


# TODO: fetch distributor products - set many=True
class DistributorSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=False, required=False, many=True)

    class Meta:
        model = User

        # 'created_at', 'updated_at'
        fields = ('id', 'email', 'products', 'username', 'last_name', 'first_name',)
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(DistributorSerializer, self).get_validation_exlusions()

            return exclusions + ['id']

    def create(self, validated_data):
        # pop out products if exists
        # can not add products while doing a post, distributor ID unknown
        products = validated_data.pop('products', None)

        distributor = User.objects.create(**validated_data)
        # add products on post - since owner doesn't exist yet
        """
        owner_id = int(distributor.id)
        distributor.save()

        if products is not None:
            for product in products:
                prod = Product()

                prod.name = product.get('name')
                prod.category = product.get('category')
                prod.owner = owner_id

                prod.save()
                distributor.products.add(prod)
        """

        distributor.save()
        return distributor

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)

        instance.username = validated_data.get('username', None)
        instance.email = validated_data.get('email', None)
        instance.last_name = validated_data.get('last_name', None)
        instance.first_name = validated_data.get('first_name', None)

        # delete products not included in the update
        """
        if products is not None:
            print products[0]['name']
            product_ids = [product['id'] for product in products]
            for product in instance.products:
                if product.id not in product_ids:
                    product.delete()

        # create or update page instances
        for product in validated_data['products']:
            product = Product(id=product['id'], name=product['name'],
                              category=product['category'], owner=instance)
            product.save()
        """
        if products is not None:
            for product in products:
                prod = Product()

                prod.name = product.get('name')
                prod.category = product.get('category')
                prod.owner = product.get('owner')

                prod.save()
                instance.products.add(prod)

        instance.save()
        return instance