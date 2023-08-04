from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
import requests
from love_bridge.settings import SOCIAL_OUTH_CONFIG
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user) 
            return redirect('index.html')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None :
            login(request, user)
            print("로그인 성공")
            return redirect('index.html')
        else :
            return render(request, 'form_errors.html')
    else :   
        return render(request, 'login.html')
    
def logout(request):
    logout(request)
    return redirect('home')

@api_view(['GET'])
@permission_classes([AllowAny, ])
def kakao_get_login(request):
    CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRECT_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
        CLIENT_ID, REDIRECT_URL)
    res = redirect(url)
    return res


@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_user_info(reqeust):
    CODE = reqeust.query_params['code']
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