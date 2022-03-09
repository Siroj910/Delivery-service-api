
#serializers
from .serializers import MarketSerializer, MenuSerializer

#models
from .models import MarketName, MenuObject

#rest framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class MarketViewSet(ModelViewSet):
	queryset = MarketName.objects.all()
	serializer_class = MarketSerializer


	@action(detail=True, methods=['GET'])
	def menu(self, request, *args ,**kwargs):

		marketname = self.get_object()
		serializer = MenuSerializer(marketname.menuobject_set.all(), many=True)

		return Response(serializer.data)

class MenuViewSet(ModelViewSet):
	queryset = MenuObject.objects.all()
	serializer_class = MenuSerializer


