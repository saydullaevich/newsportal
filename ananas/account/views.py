from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer, PasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class RegistrationView(APIView):
    permission_classes = (~IsAuthenticated, )

    def post(self, request):
        data = RegistrationSerializer(data=request.data)
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors
            })

        user = data.save()
        user.set_password(data.validated_data.get('password'))
        user.save()

        return Response({
            "status": "success"
        })

class LoginView(APIView):
    permission_classes = (~IsAuthenticated, )
    def post(self, request):
        data = LoginSerializer(data=request.data)
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors
            })

        user = authenticate(request, **data.validated_data)
        if user is None:
            return Response({
                "status": "fail",
                "data": {
                    "password": ["Login va/yoki parol noto'g'ri"]
                }
            })

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "status": "success",
            "data": {
                "user": ProfileSerializer(user).data,
                "token": token.key
            }
        })

class ProfileView(APIView):
    def post(self, request):
        data = ProfileSerializer(data=request.data, instance=request.user)
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors
            })
        data.save()

        return Response({
            "status": "success"
        })

class PasswordChangeview(APIView):
    def post(self, request):
        data = PasswordSerializer(data=request.data, context={
            "user": request.user
        })
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors
            })

        request.user.set_password(data.validated_data.get('new_password'))
        request.user.save()

        return Response({
            'status': "success"
        })

