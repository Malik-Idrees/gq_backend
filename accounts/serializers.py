from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth import get_user_model
# User = get_user_model
from .models import User


class UserSerializerWithToken(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['email','username','access_token'] 
    
    def get_access_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)