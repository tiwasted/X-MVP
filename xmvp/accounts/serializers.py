# from django.contrib.auth import authenticate
# from rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import CustomUser
#
#
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email')
#
# class EmployerLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     tokens = serializers.SerializerMethodField()
#
#     def get_tokens(self, obj):
#         user = CustomUser.objects.get(username=obj['username'])
#         refresh = RefreshToken.for_user(user)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#
#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')
#         user = authenticate(username=username, password=password)
#         if user and user.is_active:
#             return {'username': user.username}
#         raise serializers.ValidationError('Unable to log in with provided credentials.')
