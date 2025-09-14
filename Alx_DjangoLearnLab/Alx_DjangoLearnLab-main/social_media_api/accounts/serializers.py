from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token


class RegistrationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        # Use get_user_model() directly to match the error's expectation
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        Token.objects.create(user=user)
        return user
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                data['token'] = token.key
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return data