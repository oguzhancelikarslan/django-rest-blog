from django.urls import path
from django.views.decorators.cache import cache_page

from post.api.views import (
                            PostListAPIView,
                            PostDetailAPIView,
                            PostUpdatePIView,
                            PostCreateAPIView,
                        )
app_name = "post"
urlpatterns = [
    path('list', cache_page(60 * 1)(PostListAPIView.as_view()), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('update/<slug>', PostUpdatePIView.as_view(), name='update'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
]


