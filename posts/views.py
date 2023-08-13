from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse,JsonResponse
import json
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import date
from accounts import views as accounts_views


@api_view(['GET'])
def get_programs(request):
    if request.method == 'GET':
        # programs = Program.objects.all()
        # serializer = ProgramSerializer(programs, many=True)
        # return Response(serializer.data)
        programs = Program.objects.all()                                    # 프로그램 신청 버튼 눌렀을 때 테스트
        return render(request, 'programs.html', {'programs':programs})      # 프로그램 신청 버튼 눌렀을 때 테스트


@api_view(['GET'])
def search(request):
    region = request.GET.get('region')  # 클라이언트가 요청한 지역 값
    category = request.GET.get('category')  # 클라이언트가 요청한 카테고리 값
    sorting = request.GET.get('sorting')  # 클라이언트가 요청한 검색정렬 값

    programs = Program.objects.all()

    if region:
        programs = programs.filter(district=region)
    
    if category:
        programs = programs.filter(category=category)

    if sorting == 'latest':
        programs = programs.order_by('-id')
    elif sorting == 'popular':
        programs = programs.order_by('-like')
    elif sorting == 'deadline':
        programs = programs.order_by('deadline_yy', 'deadline_mm', 'deadline_dd')

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
        top10 = Program.objects.order_by('deadline_yy', 'deadline_mm', 'deadline_dd')[:10]
        serializer = RecommendSerializer(top10, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_programs(request, pk):
    # if not request.user.is_authenticated:    # 로그인 안되어 있을 경우 신청 불가
    #     return redirect(accounts_views.home)

    program = get_object_or_404(Program, pk=pk)
    user = request.user                      # request.user : 현재 로그인한 유저
    message = "NULL"
    if program.registered_users.filter(id=user.id).exists(): # 이미 신청한 유저일 때
        program.registered_users.remove(user.id)         # 신청 취소
        program.ifregister = 0
        message = "신청 취소"
    else:                                             # 신청하지 않은 유저일 때
        program.registered_users.add(user.id)            # 신청 완료
        program.ifregister = 1
        message = "신청 완료"
    return render(request, 'detail.html', {"program":program, "message":message})