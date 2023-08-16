from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "mypage"

router=routers.DefaultRouter()
router.register('documents', MyDocumentViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('myprograms/', get_my_programs, name='myprograms'),
    path('myprograms/<int:post_id>/', delete_my_program, name='delete-myprogram'),
    path('mylike/', get_like_programs, name='like'),
]