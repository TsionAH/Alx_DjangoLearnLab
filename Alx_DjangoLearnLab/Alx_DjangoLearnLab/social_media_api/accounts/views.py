from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework import status
from .serializers import RegistrationSerialzer, LoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 



# Create your views here.

class RegistrationView(APIView):
    # This should be a single class, not a list
    serializer_class = RegistrationSerialzer
    # Allow any user (even unauthenticated) to access this view
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        # Check if the data is valid
        serializer.is_valid(raise_exception=True)
        
        # The serializer's create() method will be called to save the user
        serializer.save()
        
        # Return a successful response
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)