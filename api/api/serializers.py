from rest_framework import serializers
from ..geeksApi.models import Appointment, CustomUser


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('appointment_id', 'appointment_date', 'appointment_user')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
