from django.urls import path, include
from rest_framework import routers
from mypage import views
from mypage.views import DocumentModelViewSet

app_name = "mypage"

router=routers.DefaultRouter()
router.register('mydocuments', DocumentModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('documents/', views.documents, name='documents'),
    path('myprograms/', views.get_my_programs, name='myprograms'),
    path('like/', views.get_like_programs, name='like'),
]