from django.urls import path, include
from .views import MarketViewSet, MenuViewSet,ForUserModelViewSet
	#routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('magazines', MarketViewSet)
router.register('menu', MenuViewSet)
router.register('register', ForUserModelViewSet)




urlpatterns = [
    path('get/', include(router.urls))
    # path()asd asda asda sdasd asd adasd asd
]










