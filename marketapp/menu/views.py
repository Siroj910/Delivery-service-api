
#serializers
from .serializers import MarketSerializer, MenuSerializer,ForUserSerializer

#models
from .models import MarketName, MenuObject,ForUserReservation

#rest framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny



class MarketViewSet(ModelViewSet):
	queryset = MarketName.objects.all()
	serializer_class = MarketSerializer

	http_method_names = ['get']

	@action(detail=True, methods=['GET'])
	def menu(self, request, *args ,**kwargs):

		marketname = self.get_object()
		serializer = MenuSerializer(marketname.menuobject_set.all(), many=True)


		return Response(serializer.data)


class MenuViewSet(ModelViewSet):
	queryset = MenuObject.objects.all()
	serializer_class = MenuSerializer



class ForUserModelViewSet(ModelViewSet):

	http_method_names = ['post']
	permission_classes = [AllowAny]
	queryset = ForUserReservation.objects.all()
	serializer_class = ForUserSerializer












