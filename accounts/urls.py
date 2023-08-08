from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views
from .views import get_kakao_login, get_kakao_user_info, get_naver_login, get_naver_user_info

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/kakao/', get_kakao_login),
    path('login/kakao/user/callback/', get_kakao_user_info, name="kakao_callback"),
    path('login/naver/', get_naver_login),
    path('login/naver/user/callback/', get_naver_user_info, name="naver_callback"),
]
