from django.urls import path
from .views import FriendRequestAcceptAPI,FriendRequestRejectAPI,FriendRequestSendAPI,ListFriendRequestAPI
urlpatterns = [

  path("list-friend-request",ListFriendRequestAPI.as_view()),
  path("friend-request-send",FriendRequestSendAPI.as_view()),
  path("friend-request-accept",FriendRequestAcceptAPI.as_view()),
  path('friend-request-reject',FriendRequestRejectAPI.as_view()),
]