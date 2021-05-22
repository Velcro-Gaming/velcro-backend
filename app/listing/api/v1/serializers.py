from rest_framework import serializers

from listing.models import Listing
from game.models import Game

from accounts.api.v1.serializers import UserLiteSerializer
from game.api.v1.serializers import GameLiteSerializer
from console.api.v1.serializers import ConsoleSerializer

# Enter your Serializers

# class ListingsGameSerializer(serializers.Serializer):
#     query = serializers.CharField(write_only=True)
#     games = GameLiteSerializer(many=True)
    

class ListingLiteSerializer(serializers.ModelSerializer):
    owner = UserLiteSerializer()

    class Meta:
        model = Listing
        fields = [
            'id',
            'owner',
            'console', 'game', 'original_case',
            'swap',
            'rent', 'rent_amount',
            'sell', 'sell_amount',
            'status',
        ]

    def to_representation(self, obj):
        # request = self.context.get('request')
        data = super(ListingLiteSerializer, self).to_representation(obj)
        # Display Serialized Console object
        data['console'] = ConsoleSerializer(obj.console).data
        return data


class ListingSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = [
            'id',
            'console', 'game', 'original_case',
            'swap',
            'rent', 'rent_amount',
            'sell', 'sell_amount',
            'orders',
            'status',
        ]

    def to_representation(self, obj):
        request = self.context.get('request')
        data = super(ListingSerializer, self).to_representation(obj)
        # Display Serialized Console object
        data['game'] = GameLiteSerializer(obj.game, context={'request': request}).data
        return data

    def get_orders(self, obj):
        return {
            "count": 3,
            "earned": 30000.00
        }


class ListingsGameSerializer(serializers.Serializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    def to_representation(self, obj):
        request = self.context.get('request')
        data = super(ListingsGameSerializer, self).to_representation(obj)
        # Display Serialized Game object
        games = obj.get('games')
        data['games'] = GameLiteSerializer(games, many=True, context={'request': request}).data
        return data


class GameListingsSerializer(serializers.ModelSerializer):
    consoles = ConsoleSerializer(many=True)
    listings = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        fields = [
            'id',
            'name', 'slug',
            'category', 'consoles', 'listings',
            'image',
        ]

    def get_listings(self, game):
        listings = game.listings.all()
        return ListingLiteSerializer(listings, many=True).data