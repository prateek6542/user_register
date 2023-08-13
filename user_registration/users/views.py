from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    template_name = None 
    
    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.id)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)    