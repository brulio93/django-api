from django.shortcuts import render
from rest_framework import generics
from .models import Appointment
from ..api.serializers import AppointmentSerializer

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


