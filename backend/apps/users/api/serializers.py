from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    fullName = serializers.CharField(source='get_full_name')
    profilePicture = serializers.ImageField(source='profile_picture')
    shareEmail = serializers.BooleanField(source='share_email')
    sharePhone = serializers.BooleanField(source='share_phone')
    phoneNumber = serializers.CharField(source='phone_number')
    superUser = serializers.BooleanField(source='is_superuser')
    dateJoined = serializers.CharField(source='date_joined')
    lastLogin = serializers.CharField(source='last_login')

    class Meta:
        model = User
        fields = (
            'id',
            'firstName',
            'lastName',
            'fullName',
            'email',
            'profilePicture',
            'phoneNumber',
            'shareEmail',
            'sharePhone',
            'description',
            'superUser',
            'lastLogin',
            'dateJoined',
        )
