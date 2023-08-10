from rest_framework.serializers import ModelSerializer
from .models import Document

class DocumentModelSerializer(ModelSerializer):
    class Meta:
        model=Document
        fields='__all__'