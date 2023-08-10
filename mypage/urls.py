from django.urls import path, include
from rest_framework import routers
from mypage import views
from mypage.views import DocumentModelViewSet
app_name = "mypage"

router=routers.DefaultRouter()
router.register('Document', DocumentModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('documents/', views.documents, name='documents'),
    path('programs/', views.programs, name='programs'),
]