from django.db import models
from django.utils.translation import gettext_lazy as _


class Doctor(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    specialization = models.CharField(_("Specialization"), max_length=50)
    contact_number = models.CharField(_("Contact Number"), max_length=50)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    contact_number = models.CharField(_("Contact Number"), max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name="patient")
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name="patient")
    date_admitted = models.DateField(_("Date Admitted"))

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    patient = models.ManyToManyField(Patient, related_name="hospital")
    doctor = models.ManyToManyField(Doctor, related_name="hospital")
    nurse = models.ManyToManyField(Nurse, related_name="hospital")

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="medical_record"
    )
    diagnoses = models.TextField()
    prescription = models.TextField()
