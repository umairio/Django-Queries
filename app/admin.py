from django.contrib import admin
from .models import Patient, Doctor, Nurse, Hospital, MedicalRecord


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "get_doctor_names",
        "get_nurse_name",
        "date_admitted",
    )
    list_filter = ("date_admitted", "doctor")

    def get_doctor_names(self, obj):
        return ", ".join([doctor.name for doctor in obj.doctor.all()])

    get_doctor_names.short_description = "Doctors"

    def get_nurse_name(self, obj):
        return obj.nurse.name if obj.nurse else "-"

    get_nurse_name.short_description = "Nurse"


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "contact_number")


class NurseAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_number")


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "diagnoses", "prescription")


admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Hospital)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
