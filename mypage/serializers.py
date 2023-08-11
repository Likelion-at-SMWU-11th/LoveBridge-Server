from rest_framework.serializers import ModelSerializer
from .models import Document
from posts.models import Program

class DocumentModelSerializer(ModelSerializer):
    class Meta:
        model=Document
        fields='__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model=Program
        fields=['title', 'district', 'deadline_yy', 'deadline_mm', 'deadline_dd']