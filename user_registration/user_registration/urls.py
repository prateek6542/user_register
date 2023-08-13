from django.contrib import admin
from django.urls import path
from users.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
]
