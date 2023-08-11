from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "posts"

urlpatterns = [
<<<<<<< HEAD
    path('popular/', get_popular, name="popular"),
=======
    path('programs/', get_programs, name="programs"),
    path('popular/', get_popular, name="popular"),
    path('imminent/', get_imminent, name="imminent"),
>>>>>>> 8b5f1c46b14c66e8b3a76861d7f4f5777b30a6bb
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)