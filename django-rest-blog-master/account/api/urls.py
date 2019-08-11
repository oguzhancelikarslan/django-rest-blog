from django.urls import path
from account.api.views import (
                        ProfileView,
                        UpdatePassword,
                        CreateUserView
                        )
app_name = "account"
urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
    path('change-password', UpdatePassword.as_view(), name='change-password'),
    path('register', CreateUserView.as_view(), name='register'),
]

