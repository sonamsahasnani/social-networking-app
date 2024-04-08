from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,ListUsersAPIView
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('list-all-users',ListUsersAPIView.as_view())
]