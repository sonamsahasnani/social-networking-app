from rest_framework import serializers
#from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["id", "first_name", "last_name", "username"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=CustomUser.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  
  class Meta:
    model = CustomUser
    fields = ('username', 'password',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': False},
      'last_name': {'required': False}
    }
  
  def create(self, validated_data):
    username=validated_data.get('username',None)
    first_name=validated_data.get('first_name',"")
    last_name=validated_data.get('last_name',"")
    user = CustomUser.objects.create(
      username=username,
      email=validated_data['email'],
      first_name=first_name,
      last_name=last_name
    )
    user.set_password(validated_data['password'])
    user.save()
    return user