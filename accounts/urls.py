from django.urls import path, include
from accounts import views
from .views import kakao_get_login, get_user_info

app_name = "accounts"

urlpatterns = [
    path('login/kakao/', kakao_get_login),
    path('login/kakao/user/callback/', get_user_info, name="kakao_callback"),
]
