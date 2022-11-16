from rest_framework import serializers
from .models import Raport

class RaportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raport
        fields = "__all__"