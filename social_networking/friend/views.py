from django.shortcuts import render

# Create your views here

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from user.models import CustomUser
from .models import FriendRequest


#Class based view to register user
class FriendRequestSendAPI(generics.CreateAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def create(self,request,*args,**kwargs):
    try:
        from_user=request.user
        print(from_user)
        to_user_id=request.data.get('to_user_id')
        to_user=CustomUser.objects.get(id=to_user_id)
        fr=FriendRequest.objects.create(to_id=to_user,from_id=from_user)
        fr.save()
        return Response({"message":"FriendRequest sent successfully"})
    except Exception as e:
        print("failed due to {}".format(e))
        return Response({"message":"FriendRequest failed"})
  
class FriendRequestAcceptAPI(generics.UpdateAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def update(self,request,*args,**kwargs):
    from_user=request.user
    from_user_id=request.data.get('from_user_id')
    from_user=CustomUser.objects.get(id=from_user_id)
    fr=FriendRequest.objects.get(to_id=request.user,from_id=from_user)
    fr.accepted=True
    fr.save()
    return Response({"message":"FriendRequest Accepted successfully"})
  
class FriendRequestRejectAPI(generics.DestroyAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def delete(self,request,*args,**kwargs):
    from_user_id=request.data.get('from_user_id')
    from_user=CustomUser.objects.get(id=from_user_id)
    fr=FriendRequest.objects.get(to_id=request.user,from_id=from_user)
    fr.delete()
    return Response({"message":"FriendRequest Deleted successfully"})


class ListFriendRequestAPI(generics.ListAPIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def get(self,request,*args,**kwargs):
    fr=FriendRequest.objects.filter(to_id=request.user,accepted=False)
    print(fr)
    for i in fr:
        print(i.from_id)
    return Response({"message":"FriendRequest Deleted successfully"})





