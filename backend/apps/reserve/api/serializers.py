from rest_framework import serializers, exceptions

from apps.reserve.models import Reserve
from apps.base.models import Laboratory
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from apps.base.api.serializers import LaboratorySerializer


class ReserveSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='update_at', read_only=True)
    laboratory = LaboratorySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    laboratory_id = serializers.IntegerField(write_only=True)
    user_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Reserve
        fields = (
            'id',
            'user',
            'laboratory',
            'date',
            'initial_time',
            'end_time',
            'status',
            'obs',
            'createdAt',
            'updatedAt',
            'laboratory_id',
            'user_id',
        )

    def create(self, validated_data):
        if Reserve.objects.filter(
                date=validated_data['date'],
                initial_time__range=(validated_data['initial_time'], validated_data['end_time'])):
            raise exceptions.ParseError(detail="Já existe reserva nesta data")

        user_id = validated_data.pop('user_id')
        laboratory_id = validated_data.pop('laboratory_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.NotFound(detail="Usuário não encontrado")
        try:
            laboratory = Laboratory.objects.get(id=laboratory_id)
        except Laboratory.DoesNotExist:
            raise exceptions.NotFound(detail="Laboratório não encontrado")
        reserve = Reserve.objects.create(**validated_data, laboratory=laboratory, user=user)
        reserve.save()
        return reserve

