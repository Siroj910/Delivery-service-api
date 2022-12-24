
#serializers
from .serializers import MarketSerializer, MenuSerializer,ForUserSerializer

#models
from .models import MarketName, MenuObject,ForUserReservation

#rest framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# telebot setting
import telebot

token = '1732354024:AAFi0n2Q9U0BTk-fbFaL9Rh9pIMTRIIZgeE'
bot = telebot.TeleBot(token)

# json 
import json
 
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

	def create(self, request):
		post_data = request.data.dict()
		order = []
		
		for post in post_data.values():
			order.append(post)

		list_product = order[7]
		dict_maker = json.loads(list_product)
		
		a = []
		for product in dict_maker:
			title = product['title']
			price = product['price']

			a.append(title)
			a.append(price)

		txt = f""" 
			Name: {order[1]}
			Full adress:{order[2]}
			Phone num:{order[3]}

			Summa:{order[6]}
			
			Products:{a}
			"""

		lon = float(order[4])
		lat = float(order[5])

		bot.send_location(1260142263, latitude=lat, longitude=lon)
		bot.send_message(1260142263,txt )


		return Response(data="HAVE POSTED")



def proba(request):
	return "Hello world"






