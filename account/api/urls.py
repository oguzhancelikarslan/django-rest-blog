from django.urls import path
from account.api.views import (
                        ProfileView
                        )
app_name = "acoount"
urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
]

