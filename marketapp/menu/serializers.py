from rest_framework import serializers

from .models import MarketName, MenuObject

class MarketSerializer(serializers.ModelSerializer):
	class Meta:
		model = MarketName
		fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuObject
		fields = '__all__'









