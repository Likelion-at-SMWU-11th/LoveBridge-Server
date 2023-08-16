from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .models import *
from programs.models import *
from .serializers import *
from programs.serializers import *


def home(request):
    return render(request, 'index.html')


class MyDocumentViewset(viewsets.ModelViewSet):
    queryset = MyDocument.objects.all()
    serializer_class = MyDocumentSerializer


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