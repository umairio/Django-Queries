### Queries Part 1

1. Retrieve all patients admitted on a specific date.

        date_pat = Patient.objects.filter(date_admitted = '2024-02-15')
2. Get the names of all doctors who have patients with a specific diagnosis.

        Doctor.objects.filter(patient__medical_record__diagnoses__icontains='off')
3. Find all patients treated by a particular nurse.

        patient_nurse = Patient.objects.filter(nurse__name='Barbara Le')
4. Retrieve the contact number of the doctor for a given patient.

        Doctor.objects.filter(patient__name = 'Christine Goodman').values('contact_number').first()
5. Get the total number of patients admitted to the hospital.

        Hospital.objects.annotate(num_patient = Count('patient')).aggregate(sun = Sum('num_patient'))
6. Find the patients who are not assigned to any nurse.

        Patient.objects.filter(nurse=None)
7. Retrieve the names of nurses who have patients with a specific prescription.

        Nurse.objects.filter(patient__medical_record__prescription__icontains='off')
8. Get the average age of patients in the hospital.
        
        Hospital.objects.annotate(avg_age = Avg('patient__age')).values("name",'avg_age')
9. Find the most recently admitted patient.
        
        Patient.objects.order_by('-date_admitted').first()
10. Retrieve all doctors who have more than five patients.
        
        Doctor.objects.annotate(no_pat = Count('patient')).filter(no_pat__gt=5)
11. Find the patients who have been admitted for more than a week.
        
        Patient.objects.filter(date_admitted__lte = timezone.now() - timedelta(days=7))
12. Get the number of patients assigned to each nurse.
        
        Nurse.objects.annotate(num_patient=Count('patient')).values_list('name','num_patient')
13. Retrieve the names of patients who have a specific doctor.
       
        Patient.objects.filter(doctor__name='Michael Weiss').values('name')
14. Find the doctors who specialize in a specific medical field.
        
        special_doc = Doctor.objects.filter(specialization__icontains = 'assistant')
15. Get the names of patients treated by a doctor with a specific specialization.
        
        Patient.objects.filter(doctor__specialization__icontains = 'assistant').values('name')
16. Find the nurses who have not been assigned any patients.
        
        happy_nurses = Nurse.objects.filter(patients=None)
17. Retrieve the latest medical record for a given patient.
        
        recent_record = MedicalRecord.objects.get(patient = 30)
18. Get the names of patients with a specific diagnosis.
        
        Patient.objects.filter(medical_record__prescription__icontains='off').values('name')
19. Find the doctors who have patients of a certain age group.
        
        Doctor.objects.filter(patient__age__lte=20)
20. Retrieve all patients with a specific prescription.
        
        Patient.objects.filter(medical_record__prescription__icontains='off')
21. Find the nurses who have patients with a specific age.
        
        Nurse.objects.get(patient__age = 18)
22. Get the total number of medical records in the system.

        MedicalRecord.objects.count()
23. Retrieve the names of patients treated by a nurse with a specific contact number.
        
        Patient.objects.filter(nurse__contact_number = '530-997-8164x11263')
24. Find the patients who are treated by more than one doctor.
        
        Patient.objects.annotate(no_doc = Count('doctor')).filter(no_doc__gt=1)
25. Get the names of doctors who have treated patients with a specific prescription.
        
        Doctor.objects.filter(patient__medical_record__prescription__icontains='off')
26. Find the patients who have not been assigned to any doctor.
        
        Patient.objects.filter(doctor=None)
27. Retrieve the doctors who have patients admitted on a specific date.
        
        Patient.objects.filter(date_admitted = '2024-02-15')
28. Get the number of patients admitted each month.
        
        Patient.objects.values("date_admitted__month").annotate(count = Count('id'))
29. Find the patients with the highest age in the hospital.
        
        Patient.objects.filter(hospital__id='3').order_by('-age').first()
30. Retrieve all nurses who have patients admitted on a specific date.
        
        Nurse.objects.filter(patient__date_admitted='2024-02-15')
31. Find the doctors who have patients with a specific age.
        
        Doctor.objects.get(patient__age = 18)
32. Get the number of patients treated by each doctor.
        
        Doctor.objects.annotate(num = Count('patient')).values_list('name','num')
33. Retrieve the names of patients with a specific age.
        
        Patient.objects.filter(age = 18)
34. Find the nurses who have patients with a specific diagnosis.
        
        Nurse.objects.filter(patient__medical_record__diagnoses__icontains='off')
35. Get the names of patients treated by a nurse with a specific contact number.
        
        Patient.objects.filter(nurse__contact_number = "834-404-9152x87947").values('name')
36. Find the doctors who have not been assigned any patients.
        
        Doctor.objects.filter(patient=None)
37. Retrieve the patients who have medical records with a specific prescription.
        
        Patient.objects.filter(medical_record__prescription__icontains='off')
38. Get the average age of patients treated by each doctor.
        
        Doctor.objects.annotate(avg_age = Avg('patient__age')).values_list('name','avg_age')
39. Find the doctors who have patients with a specific prescription.
        
        Doctor.objects.filter(patient__medical_record__prescription__icontains='off')
50. Retrieve the names of patients treated by a doctor with a specific contact number.
        
        Patient.objects.filter(doctor__contact_number = "001-827-487-2067").values('name')
51. Find the nurses who have patients with a specific prescription.
        
        Nurse.objects.filter(patient__medical_record__prescription__icontains='off')
52. Retrieve the patients who have not been assigned to any nurse.
        
        Patient.objects.filter(nurse=None)
53. Find the doctors who have patients admitted for more than a week.
        
        Doctor.objects.filter(patient__date_admitted__gt = timezone.now() - timedelta(days=7))
54. Get the names of patients with a specific diagnosis treated by a specific doctor.
        
        Patient.objects.filter(medical_record__diagnoses__icontains = 'off',doctor__name = 'Daniel Ellis')
55. Find the nurses who have patients with a specific age group.
        
        Nurse.objects.filter(patient__age__lte=20)
56. Retrieve the doctors who have patients with a specific diagnosis and age group.
        
        Doctor.objects.filter(Q(patient__age__lte=30) & Q(patient__medical_record__diagnoses__icontains = "off"))
57. Get the number of patients treated by each doctor in a specific specialization.
        
        Doctor.objects.filter(specialization__icontains = 'assistant').annotate(num = Count('patient')).values_list('name','num')
58. Find the patients who have been treated by more than one nurse.
        
        Patient.objects.annotate(no_nurse = Count('nurse')).filter(no_nurse__gt=1).values_list('name','')
59. Retrieve the names of doctors who have patients with a specific diagnosis and age group.
        
        Doctor.objects.filter(Q(patient__age__lte=30) & Q(patient__medical_record__diagnoses__icontains = "off")).values('name')