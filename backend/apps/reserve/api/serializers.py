from rest_framework import serializers

from apps.reserve.models import Reserve
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


# class ReserveSerializer(serializers.ModelSerializer):
#     createdAt = serializers.DateTimeField(source='created_at', read_only=True)
#     updatedAt = serializers.DateTimeField(source='update_at', read_only=True)
#     laboratory =
#     user = UserSerializer()
#
#     class Meta:
#         model = Reserve
#         fields = (
#             'id',
#             'user_id',
#             'laboratory_id',
#             'start_date',
#             'initial_time',
#             'end_time',
#             'end_date',
#             'status',
#             'obs',
#         )
#
#     def create(self, validated_data):
#         user_id = validated_data.pop('user_id')
#         laboratory_id = validated_data.pop('laboratory_id')
#
#         user = User.objects.get()
#         reserve = Reserve.objects.create(**validated_data)
#         reserve.save()
#         return reserve

