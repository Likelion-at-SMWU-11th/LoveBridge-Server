from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "posts"

urlpatterns = [
    path('programs/', get_programs, name="programs"),
    path('popular/', get_popular, name="popular"),
    path('imminent/', get_imminent, name="imminent"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)