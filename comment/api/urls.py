from django.urls import path
from comment.api.views import (
                            CommentCreateAPIView,
                            CommentListAPIView,
                            CommentUpdateAPIView
                        )
app_name = "comment"
urlpatterns = [
    path('create', CommentCreateAPIView.as_view(), name='create'),
    path('list', CommentListAPIView.as_view(), name='list'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),
]


