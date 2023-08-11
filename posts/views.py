from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import date


@api_view(['GET'])
def get_programs(request):
    if request.method == 'GET':
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_popular(request):
    if request.method == 'GET':
        top10 = Program.objects.all().order_by('-like')[:10]
        serializer = RecommendSerializer(top10, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_imminent(request):
    if request.method == 'GET':
        programs = Program.objects.all()
        imminent_programs = []
        for program in programs:
            today = date.today()
            deadline = date(program.deadline_yy, program.deadline_mm, program.deadline_dd)
            remaining_days = (deadline - today).days
            imminent_programs.append({
                'program': program,
                'remaining_days': remaining_days
            })
        
        imminent_programs.sort(key=lambda x: x['remaining_days'])
        top10 = imminent_programs[:10]
        serializer = RecommendSerializer([item['program'] for item in top10], many=True)

        return Response(serializer.data)