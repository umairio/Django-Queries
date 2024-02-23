from django.contrib import admin
from django.urls import include, path
from .views import index, DoctorViewSet, NurseViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("doctors", DoctorViewSet, basename="doctors")
router.register("nurses", NurseViewSet, basename="nurses")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
urlpatterns += router.urls
