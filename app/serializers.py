from django.contrib.auth.models import User
from rest_framework import serializers,pagination
from .models import Patient, Doctor, Nurse, Hospital, MedicalRecord
from rest_framework.views import APIView
from rest_framework import authentication, permissions, viewsets
from rest_framework.response import Response

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class DoctorSerializer(serializers.ModelSerializer):
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request):
        doctors = [doctor for doctor in Doctor.objects.all()]
        return Response(doctors)
    class Meta:
        model = Doctor
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request):
        nurses = [nurse for nurse in Nurse.objects.all()]
        return Response(nurses)
    class Meta:
        model = Nurse
        fields = '__all__'
