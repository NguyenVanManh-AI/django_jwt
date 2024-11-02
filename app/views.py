from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
import json

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    pass  # Sử dụng mặc định của TokenObtainPairView để xử lý login

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class Home(APIView):
    permission_classes = []  # Bỏ các lớp permission để mở endpoint này

    def get(self, request):
        data = {
            'name': 'Home (No Need Login)'
        }
        return Response(data)

class Dashboard(APIView):
    permission_classes = [IsAuthenticated]  # Yêu cầu đăng nhập (sử dụng JWT)

    def get(self, request):
        user = request.user  # Lấy đối tượng người dùng từ request

        # Lấy thông tin người dùng
        data = {
            'status': 'Dashboard (Must Login)',
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(data)