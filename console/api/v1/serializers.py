from rest_framework import serializers

from console.models import Console, UserConsole


# Enter your Serializers

class ConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = [
            'id',
            'name', 'slug', 'short_name'
        ]


class UserConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserConsole
        fields = [
            'id',
            'user', 'console',
        ]
    
    def to_representation(self, obj):
        data = super(UserConsoleSerializer, self).to_representation(obj)
        # Display Serialized Console object
        data['console'] = ConsoleSerializer(obj.console).data
        return data
