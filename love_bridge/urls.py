from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from accounts import views
from mypage import views

from django.conf.urls.static import static
=======
>>>>>>> 7e9a5e2 ([Feat] 실시간 인기글 조회 (#14))
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts import views as accounts_views
from posts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home),

    path('accounts/', include('accounts.urls', namespace='accounts')),
<<<<<<< HEAD
    path('', views.home),
    path('mypage/', include('mypage.urls')),
=======
    path('posts/', include('posts.urls', namespace='home')),
>>>>>>> 7e9a5e2 ([Feat] 실시간 인기글 조회 (#14))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
