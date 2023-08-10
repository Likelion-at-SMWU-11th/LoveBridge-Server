from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/kakao/', get_kakao_login, name='kakao'),
    path('login/kakao/user/callback/', get_kakao_user_info, name="kakao_callback"),
    
    path('login/naver/', get_naver_login, name='naver'),
    path('login/naver/user/callback/', get_naver_user_info, name="naver_callback"),
    
    path('login/google/', get_google_login, name='google'),
    path('login/google/user/callback/', get_google_user_info, name="google_callback"),
]
