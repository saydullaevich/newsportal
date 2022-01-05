from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {
                'required': True,
                'validators': [
                    MinLengthValidator(5)
                ]
            },
            'last_name': {
                'required': True
            },
            'email': {
                'required': True
            }
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {
                'required': True,
                'validators': [
                    MinLengthValidator(5)
                ]
            },
            'last_name': {
                'required': True
            },
            'email': {
                'required': True
            }
        }

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)

    def validate_old_password(self, data):
        user = self.context.get('user')

        if not user.check_password(data):
            raise ValidationError({
                "old_password": "Eski parol noto'g'ri"
            })
        return data