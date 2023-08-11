from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import DocumentForm
from .models import Document
from posts.models import Program
from .serializers import *

def home(request):
    return render(request, 'index.html')

class DocumentModelViewSet(ModelViewSet):
    queryset=Document.objects.all()
    serializer_class=DocumentModelSerializer

def documents(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        document = Document(
            imgfile=file,
        )
        document.save()
        return redirect('/mypage/programs')
    else:
        documentForm = DocumentForm
        context = {
            'documentForm': documentForm,
        }
    return render(request, 'documents.html', context)

@api_view(['GET'])
def get_like_programs(request):
    if request.method == 'GET':
        like = Program.objects.all().filter(iflike=True)
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)