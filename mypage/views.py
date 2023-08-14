from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import DocumentForm
from .models import *
from programs.models import *
from .serializers import *
from programs.serializers import *


def home(request):
    return render(request, 'index.html')


class DocumentModelViewSet(ModelViewSet):
    queryset=Document.objects.all()
    serializer_class=DocumentModelSerializer


def documents(request):  # 수정 필요
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
def get_my_programs(request):
    if request.method == 'GET':
        my_programs = MyProgram.objects.all()
        serializer = MyProgramSerializer(my_programs, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@require_http_methods(["DELETE"])
def delete_my_program(request, post_id):
    if request.method == 'DELETE':
        my_program = MyProgram.objects.get(pk=post_id)
        my_program.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
def get_like_programs(request):
    if request.method == 'GET':
        my_like = MyLike.objects.all()
        serializer = MyLikeSerializer(my_like, many=True)
        return Response(serializer.data)