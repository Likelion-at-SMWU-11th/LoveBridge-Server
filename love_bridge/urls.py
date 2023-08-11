from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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
