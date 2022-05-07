from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.serializers import UserSerializerWithToken

from django.contrib.auth import get_user_model
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["username"] = str(self.user.username)
        data["email"] = str(self.user.email)
        data["isAdmin"] = str(self.user.is_staff)

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def registerUser(req):
    data = req.data

    try:
        
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        serializer = UserSerializerWithToken(user,many=False)
        return Response(serializer.data)

    except:
        message = {'error':'User with this email already exists'}
        return Response(message)