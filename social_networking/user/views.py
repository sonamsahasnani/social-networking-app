from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
#from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from user.models import CustomUser

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class ListUsersAPIView(generics.ListAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def get(self,request,*args,**kwargs):
    users = CustomUser.objects.all()
    data=[]
    for i in users:
      d={
        "id":i.id,
        "email":i.email
      }
      data.append(d)
    #serializer = UserSerializer(users)
    return Response({"data":data})


