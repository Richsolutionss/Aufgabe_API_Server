from rest_framework import serializers
from backend2.models import Server
from backend2.models import Hersteller

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('__all__')

class HerstellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hersteller
        fields =  ('__all__')