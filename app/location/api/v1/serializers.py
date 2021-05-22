from rest_framework import serializers

from location.models import Country, State, City


# Enter your Serializers

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name', 'full_name', 'calling_code', 'iso2']

# class CountryCodeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Country
#         fields = ['id', 'name', 'full_name']


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = State
        fields = ['id', 'name', 'country']


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'state']

