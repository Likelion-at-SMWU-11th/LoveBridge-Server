from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "mypage"

# router=routers.DefaultRouter()
# router.register('mydocuments', DocumentModelViewSet)

urlpatterns = [
    # path('',include(router.urls)),
    path('documents/', documents, name='documents'),
    path('myprograms/', get_my_programs, name='myprograms'),
    path('myprograms/<int:apply_id>/', delete_my_program, name='delete-myprogram'),
    path('mylike/', get_like_programs, name='like'),
]