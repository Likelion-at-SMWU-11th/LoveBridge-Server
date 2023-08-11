from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .forms import DocumentForm
from .models import Document
from .serializers import DocumentModelSerializer

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

def programs(request):
    return render(request, 'programs.html')