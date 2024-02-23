from django.shortcuts import render

# from django.contrib.auth.models import Group, User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .serializers import DoctorSerializer, NurseSerializer
from .models import Doctor, Patient, Nurse, Hospital, MedicalRecord
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


def index(request):
    return render(request, "index.html")


class DoctorViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAdminUser]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    @action(detail=False, methods=['get'])
    def get(self, request):
        doctors = [doctor for doctor in Doctor.objects.all()]
        return Response(doctors)


class NurseViewSet(ReadOnlyModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
