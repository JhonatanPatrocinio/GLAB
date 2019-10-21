from rest_framework import serializers
from django.contrib.auth.models import User

from apps.users.models import UserApp


class UserSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='username', required=True)
    emailField = serializers.EmailField(source='email', required=True)
    firstName = serializers.CharField(source='first_name', required=True)
    lastName = serializers.CharField(source='last_name', required=True)
    fullName = serializers.CharField(source='get_full_name', required=False)
    staffUser = serializers.BooleanField(source='is_staff',required=False, read_only=True)
    isActive = serializers.BooleanField(source='is_active', required=False, read_only=True)
    superUser = serializers.BooleanField(source='is_superuser', required=False, read_only=True)
    dateJoined = serializers.CharField(source='date_joined', required=False, read_only=True)
    password1 = serializers.CharField(source='password', write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'userName',
            'emailField',
            'firstName',
            'lastName',
            'fullName',
            'staffUser',
            'isActive',
            'superUser',
            'dateJoined',
            'password1',
        )


class UserAppSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    typeUser = serializers.CharField(source='type_user', required=True)
    emailConfirm = serializers.BooleanField(source='email_confirm', required=False)
    shareEmail = serializers.BooleanField(source='share_email', required=False)
    sharePhone = serializers.BooleanField(source='share_phone', required=False)
    phoneNumber = serializers.BooleanField(source='phone_number', required=False)
    profilePicture = serializers.ImageField(source='profile_picture', required=False)

    class Meta:
        model = UserApp
        fields = (
            'id',
            'user',
            'typeUser',
            'emailConfirm',
            'shareEmail',
            'sharePhone',
            'phoneNumber',
            'profilePicture',
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user_app = UserApp.objects.create(user=user, **validated_data)
        return user_app
