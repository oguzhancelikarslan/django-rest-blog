from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include('post.api.urls', namespace='post')),
    path('api/comment/', include('comment.api.urls', namespace='comment')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
