from rest_framework.serializers import ModelSerializer
from .models import Document
from programs.models import *
from rest_framework import serializers


class DocumentModelSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields='__all__'


class MyProgramSerializer(ModelSerializer):
    title = serializers.CharField(source='program.title', read_only=True)
    district = serializers.CharField(source='program.district', read_only=True)

    class Meta:
        model = MyProgram
        fields = [f'title', 'district', 'process']


class MyLikeSerializer(ModelSerializer):
    class Meta:
        model = MyLike
        fields = '__all__'