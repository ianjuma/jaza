from rest_framework import serializers

from agents.models import Agent
from products.serializers import ProductSerializer
from products.models import Product


class AgentSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=False, required=False, many=True)

    class Meta:
        model = Agent

        fields = ('id', 'products', 'phone_number', 'name', 'pin')
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(AgentSerializer, self).get_validation_exlusions()

            return exclusions + ['id']

    def create(self, validated_data):
        # pop out products if exists
        products = validated_data.pop('products', None)

        agent = Agent.objects.create(**validated_data)
        agent.save()

        if products is not None:
            for product in products:
                prod = Product()

                prod.name = product.get('name')
                prod.category = product.get('category')
                prod.owner = product.get('owner')

                prod.save()
                agent.products.add(prod)

        agent.save()
        return agent

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)

        # update user info
        instance.phone_number = validated_data.get('phone_number', None)
        instance.pin = validated_data.get('pin', None)
        instance.name = validated_data.get('name', None)

        """
        # delete products not included in the update
        if products is not None:
            product_ids = [product['id'] for product in products]
            for product in products:
                if product.id not in product_ids:
                    product.delete()
        """

        """
        # create or update page instances
        for product in validated_data['products']:
            product = Product(id=product['id'], name=product['name'],
                              category=product['category'], owner=product['owner'], product=instance)
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