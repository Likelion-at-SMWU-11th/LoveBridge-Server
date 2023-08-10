from django.shortcuts import render,  redirect
from json import JSONDecodeError
from django.http import JsonResponse
import requests
from rest_framework import status
from .models import *
from love_bridge.settings import SOCIAL_OUTH_CONFIG
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def home(request):
    return render(request, 'index.html')

# 카카오 로그인
@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_kakao_login(request):
    CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRECT_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
        CLIENT_ID, REDIRECT_URL)
    return redirect(url)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_kakao_user_info(request):
    CODE = request.query_params['code']
    url = "https://kauth.kakao.com/oauth/token"
    res = {
        'grant_type': 'authorization_code',
        'client_id': SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
        'redirect_url': SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
        'client_secret': SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
        'code': CODE
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    response = requests.post(url, data=res, headers=headers)
    token_json = response.json()
    user_url = "https://kapi.kakao.com/v2/user/me"
    auth = "Bearer " + token_json['access_token']
    HEADER = {
        "Authorization": auth,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    res = requests.get(user_url, headers=HEADER)
    print(response.json())
    return Response(res.text)

def kakao_logout(access_token):
    logout_url = "https://kapi.kakao.com/v1/user/logout"
    auth = "Bearer " + access_token
    HEADER = {
        "Authorization": auth
    }
    response = requests.post(logout_url, headers=HEADER)
    return redirect("index.html")


# 네이버 로그인
@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_naver_login(request):
    CLIENT_ID = SOCIAL_OUTH_CONFIG['NAVER_CLIENT_ID']
    REDIRECT_URL = SOCIAL_OUTH_CONFIG['NAVER_REDIRECT_URI']
    url = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={0}&state=STATE_STRING&redirect_uri={1}".format(
        CLIENT_ID, REDIRECT_URL)
    return redirect(url)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_naver_user_info(reqeust):
    CODE = reqeust.GET.get("code")
    url = "https://nid.naver.com/oauth2.0/token"
    res = {
        'grant_type': 'authorization_code',
        'client_id': SOCIAL_OUTH_CONFIG['NAVER_CLIENT_ID'],
        'client_secret': SOCIAL_OUTH_CONFIG['NAVER_CLIENT_SECRET'],
        'code': CODE,
        'state': reqeust.GET.get("state")
    }
    response = requests.post(url, data=res)
    token_json = response.json()
    user_url = "https://openapi.naver.com/v1/nid/me"
    auth = "Bearer " + token_json['access_token']
    HEADER = {
        "Authorization": auth,
    }
    res = requests.get(user_url, headers=HEADER)
    print(response.json())
    return Response(res.text)


# 구글 로그인
@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email"
    CLIENT_ID = SOCIAL_OUTH_CONFIG['GOOGLE_CLIENT_ID']
    REDIRECT_URL = SOCIAL_OUTH_CONFIG['GOOGLE_REDIRECT_URI']
    url = "https://accounts.google.com/o/oauth2/v2/auth?client_id={0}&response_type=code&redirect_uri={1}&scope={2}".format(
        CLIENT_ID, REDIRECT_URL, scope)
    return redirect(url)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_google_user_info(reqeust):
    CODE = reqeust.GET.get("code")
    url = "https://oauth2.googleapis.com/token"
    res = {
        'client_id': SOCIAL_OUTH_CONFIG['GOOGLE_CLIENT_ID'],
        'client_secret': SOCIAL_OUTH_CONFIG['GOOGLE_CLIENT_SECRET'],
        'code': CODE,
        'grant_type': 'authorization_code',
        'redirect_uri': SOCIAL_OUTH_CONFIG['GOOGLE_REDIRECT_URI'],
        'state': reqeust.GET.get("state")
    }
    response = requests.post(url, data=res)
    token_json = response.json()
    user_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    auth = "Bearer " + token_json['access_token']
    HEADER = {
        "Authorization": auth,
    }
    res = requests.get(user_url, headers=HEADER)
    print(response.json())
    return Response(res.text)