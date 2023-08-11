from django.contrib import admin
<<<<<<< Updated upstream
=======
from django.urls import path, include
from accounts import views
from mypage import views
from django.conf.urls.static import static
>>>>>>> Stashed changes
from django.conf import settings

<<<<<<< Updated upstream
=======
from mypage import views
>>>>>>> Stashed changes
from accounts import views as accounts_views
from posts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('posts/', include('posts.urls', namespace='home')),
    path('mypage/', include('mypage.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
