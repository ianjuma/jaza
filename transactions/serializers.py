from rest_framework import serializers

from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        distributor = serializers.RelatedField('Distributor')
        agent = serializers.RelatedField('Agent')
        product = serializers.RelatedField('Product')

        fields = ('id', 'quantity', 'created_at', 'updated_at',
                  'price_per_unit', 'percent_discount', 'distributor',
                  'agent', 'product')

        read_only_fields = ('id', 'created_at', 'updated_at', 'agent', 'distributor', 'product')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Transaction, self).get_validation_exlusions()

            return exclusions + ['price_per_unit']