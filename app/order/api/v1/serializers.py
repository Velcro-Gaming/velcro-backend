from rest_framework import serializers

from order.models import Order


# Enter your Serializers

class OrderSerializer(serializers.ModelSerializer):
    offered_listings = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = Order
        fields = [
            'id',
            'reference',
            'owner', 'listing',
            '_type',
            'fee', 'duration', 'offered_listings',
        ]
        

