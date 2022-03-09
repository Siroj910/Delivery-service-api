from django.urls import path, include
from .views import MarketViewSet, MenuViewSet
	#routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('magazines', MarketViewSet)
router.register('menu', MenuViewSet)




urlpatterns = [
    path('get/', include(router.urls))
]










