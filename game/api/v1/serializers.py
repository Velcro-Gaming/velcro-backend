from rest_framework import serializers

from game.models import Game
from console.models import Console

from console.api.v1.serializers import ConsoleSerializer
# from listing.api.v1.serializers import ListingLiteSerializer

# Enter your Serializers

class GameLiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = [
            'id',
            'name', 'slug',
            'category', 'image',
        ]


class GameSerializer(serializers.ModelSerializer):
    consoles = serializers.PrimaryKeyRelatedField(many=True, queryset=Console.objects.all())
    
    class Meta:
        model = Game
        fields = [
            'id',
            'name', 'slug',
            'category', 'consoles',
            'image',
        ]

    def to_representation(self, obj):
        data = super(GameSerializer, self).to_representation(obj)
        # Display Serialized Console object
        data['consoles'] = ConsoleSerializer(obj.consoles, many=True).data
        return data


    # def to_representation(self, obj):
    #     data = super(GameSerializer, self).to_representation(obj)
    #     # Display Serialized Console object
    #     data['consoles'] = ConsoleSerializer(obj.consoles, many=True).data
    #     return data
