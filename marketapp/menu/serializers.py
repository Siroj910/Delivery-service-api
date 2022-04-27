from rest_framework import serializers

from .models import MarketName, MenuObject,ForUserReservation

class MarketSerializer(serializers.ModelSerializer):
	class Meta:
		model = MarketName
		fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuObject
		fields = '__all__'

class ForUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = ForUserReservation
		fields = '__all__'










