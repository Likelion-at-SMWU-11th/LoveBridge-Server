from rest_framework.serializers import ModelSerializer
from .models import *


class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class RecommendSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = ['image', 'title', 'district']