from rest_framework import serializers
from .models import *


class PriceInterCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInterCity
        fields = "__all__"
        depth = 2


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class BookingInterCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInterCity
        fields = "__all__"
        depth = 1


class BookingInCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInterCity
        fields = "__all__"
        depth = 1
