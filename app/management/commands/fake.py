import random
from django.core.management.base import BaseCommand
from app.models import Patient, Doctor

class Command(BaseCommand):
    help = 'Randomly assigns doctors to patients'

    def handle(self, *args, **kwargs):
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()

        for patient in patients:
            # Choose a random set of doctors
            num_doctors = random.randint(1, 3)
            random_doctors = set(random.sample(list(doctors), num_doctors))

            # Assign doctors to patient
            patient.doctor.set(random_doctors)

            self.stdout.write(self.style.SUCCESS(
                f"Assigned {len(random_doctors)} doctors to {patient.name}"
            ))
