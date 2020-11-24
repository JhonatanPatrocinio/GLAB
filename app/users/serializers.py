from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    fullName = serializers.ReadOnlyField(source='get_full_name')
    staffUser = serializers.ReadOnlyField(source='is_staff')
    isActive = serializers.BooleanField(source='is_active', required=False)
    superUser = serializers.ReadOnlyField(source='is_superuser')
    dateJoined = serializers.ReadOnlyField(source='date_joined')
    emailConfirm = serializers.BooleanField(source='email_confirm', required=False)
    shareEmail = serializers.BooleanField(source='share_email', required=False)
    sharePhone = serializers.BooleanField(source='share_phone', required=False)
    phoneNumber = serializers.BooleanField(source='phone_number', required=False, allow_null=True)
    profilePicture = serializers.ImageField(source='profile_picture', required=False, allow_null=True)
    bioDescription = serializers.CharField(source='description', required=False, allow_null=True)

    password1 = serializers.CharField(source='password', write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'fullName', 'staffUser', 'isActive', 'superUser', 'dateJoined',
            'type_user', 'emailConfirm', 'shareEmail', 'sharePhone', 'phoneNumber', 'profilePicture', 'bioDescription',
            'password1'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


