from django.urls import include, path
from rest_framework import routers

from backend2 import views

router = routers.DefaultRouter()
router.register(r'server', views.ServerViewSet)
router.register(r'Hersteller', views.HerstellerViewSet)

urlpatterns = [
    path('', include(router.urls))
]