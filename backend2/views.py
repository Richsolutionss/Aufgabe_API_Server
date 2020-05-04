from rest_framework import viewsets

from backend2.models import Server
from backend2.models import Hersteller

from backend2.serializers import ServerSerializer
from backend2.serializers import HerstellerSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class HerstellerViewSet(viewsets.ModelViewSet):
    queryset = Hersteller.objects.all()
    serializer_class = HerstellerSerializer

