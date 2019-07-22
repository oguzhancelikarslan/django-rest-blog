from django.urls import path

from favourite.api.views import FavouriteListCreateAPIView, FavouriteAPIView

app_name = "favourite"
urlpatterns = [
    path('list-create', FavouriteListCreateAPIView.as_view(), name='list-create'),
    path('update-delete/<pk>', FavouriteAPIView.as_view(), name='update-delete'),
]


