### Queries Part 1

1. Retrieve all patients admitted on a specific date.

        date_pat = Patient.objects.filter(date_admitted = '2024-02-15')
2. Get the names of all doctors who have patients with a specific diagnosis.

        spec_pat = MedicalRecord.objects.filter(diagnoses__icontains='off')
        patients_with_diagnosis = Patient.objects.filter(medical_record__in=spec_pat)
        doc_spec_pat = Doctor.objects.filter(patient__in=patients_with_diagnosis)
3. Find all patients treated by a particular nurse.

        patient_nurse = Patient.objects.filter(nurse__name='Barbara Le')
4. Retrieve the contact number of the doctor for a given patient.

        docs = Doctor.objects.filter(patient__name = 'Christine Goodman')
5. Get the total number of patients admitted to the hospital.

        python num_patients = Patient.objects.count()

6. Find the patients who are not assigned to any nurse.

        python sad_patients = Patient.objects.filter(nurse=None)

7. Retrieve the names of nurses who have patients with a specific prescription.

        spec_pat = MedicalRecord.objects.filter(prescription__icontains='off')
        patients_with_pres = Patient.objects.filter(medical_record__in=spec_pat)
        doc_spec_pat = Doctor.objects.filter(patient__in=patients_with_pres)
8. Get the average age of patients in the hospital.
        
        avg_age = Patient.objects.aggregate(Avg('age'))
9. Find the most recently admitted patient.
        
        latest_pat = Patient.objects.order_by('date_admitted').last()
10. Retrieve all doctors who have more than five patients.
        
        no_pat = Doctor.objects.annotate(no_pat = Count('patients')).filter(no_pat__lte=5)
11. Find the patients who have been admitted for more than a week.
        
        chill_pat = Patient.objects.filter(date_admitted__gt = '2024-02-12')
12. Get the number of patients assigned to each nurse.
        
        nurs = Nurse.objects.annotate(num_patients=Count('patients'))
13. Retrieve the names of patients who have a specific doctor.
       
        patients_with_doc = Patient.objects.filter(doctor__name='Michael Weiss')
14. Find the doctors who specialize in a specific medical field.
        
        special_doc = Doctor.objects.filter(specialization__icontains = 'assistant')
15. Get the names of patients treated by a doctor with a specific specialization.
        
        patients_with_doc = Patient.objects.filter(doctor=special_doc[0])
16. Find the nurses who have not been assigned any patients.
        
        happy_nurses = Nurse.objects.filter(patients=None)
17. Retrieve the latest medical record for a given patient.
        
        recent_record = MedicalRecord.objects.get(patient = 30)

18. Get the names of patients with a specific diagnosis.
        
        spec_pat = MedicalRecord.objects.filter(prescription__icontains='off')
19. Find the doctors who have patients of a certain age group.
        
        kids_doc = Doctor.objects.filter(patient__age__range = (0,20))
        kids_doc = Doctor.objects.filter(patient__age__lte=20)
20. Retrieve all patients with a specific prescription.
        
        pec_pat = MedicalRecord.objects.filter(prescription__icontains='off')
21. Find the nurses who have patients with a specific age.
        
        kids_nurse = Nurse.objects.get(patient__age = 18)
22. Get the total number of medical records in the system.
        num_mr = MedicalRecord.objects.count()
23. Retrieve the names of patients treated by a nurse with a specific contact number.
        
        kyle_pat = Patient.objects.filter(nurse__contact_number = '530-997-8164x11263')
24. Find the patients who are treated by more than one doctor.
        
        no_doc = Patient.objects.annotate(no_doc = Count('doctor')).filter(no_doc__lte=1)
25. Get the names of doctors who have treated patients with a specific prescription.
        
        spec_pat = MedicalRecord.objects.filter(prescription__icontains='off')
26. Find the patients who have not been assigned to any doctor.
        
        dying_pat = Patient.objects.filter(doctor=None)
27. Retrieve the doctors who have patients admitted on a specific date.
        
        today_pat = Patient.objects.filter(date_admitted = '2024-02-15')
28. Get the number of patients admitted each month.
        
        Patient.objects.values("date_admitted__month").annotate(count = Count('id'))
29. Find the patients with the highest age in the hospital.
        
        oldest_pat = Patient.objects.order_by('age').last()
30. Retrieve all nurses who have patients admitted on a specific date.
        
        nurses_on_date = Nurse.objects.filter(patient__date_admitted='2024-02-15')
31. Find the doctors who have patients with a specific age.
        
        kids_doc = Doctor.objects.get(patient__age = 18)
32. Get the number of patients treated by each doctor.
        
        num_pat = Doctor.objects.annotate(num = Count('patients'))
33. Retrieve the names of patients with a specific age.
        
        young_pat = Patient.objects.filter(age = 18)
34. Find the nurses who have patients with a specific diagnosis.
        
        MedicalRecord.objects.get(diagnoses__icontains =  'four along').patient.nurse
35. Get the names of patients treated by a nurse with a specific contact number.
        
        nurs = Nurse.objects.filter(contact_number = "834-404-9152x87947")
        Patient.objects.filter(nurse=nurs[0])
36. Find the doctors who have not been assigned any patients.
        
        wellay_doc = Doctor.objects.filter(patient=None)
37. Retrieve the patients who have medical records with a specific prescription.
        
        spec_pat = Patient.objects.filter(medical_record__prescription__icontains='off')
38. Get the average age of patients treated by each doctor.
        
        avg_age_pat = Doctor.objects.annotate(avg_age = Avg('patient__age'))
39. Find the doctors who have patients with a specific prescription.
        
        spec_pat = MedicalRecord.objects.filter(prescription__icontains='off')
50. Retrieve the names of patients treated by a doctor with a specific contact number.
        
        Patient.objects.filter(doctor__contact_number = "001-827-487-2067")
51. Find the nurses who have patients with a specific prescription.
        
        Nurse.objects.filter(patient__medical_record__prescription__icontains='off')
52. Retrieve the patients who have not been assigned to any nurse.
        
        sad_pat = Patient.objects.filter(nurse=None)
53. Find the doctors who have patients admitted for more than a week.
        
        Doctor.objects.filter(patient__date_admitted__gt = '2024-02-12' )
54. Get the names of patients with a specific diagnosis treated by a specific doctor.
        
        Patient.objects.filter(medical_record__diagnoses__icontains = 'off',doctor__name = 'Daniel Ellis')
55. Find the nurses who have patients with a specific age group.
        
        Nurse.objects.filter(patient__age__lte=20)
56. Retrieve the doctors who have patients with a specific diagnosis and age group.
        
        Doctor.objects.filter(patient__age__lte=20, patient__medical_record__diagnoses__icontains = "off")
        Doctor.objects.filter(Q(patient__age__lte=30) & Q(patient__medical_record__diagnoses__icontains = "off"))
57. Get the number of patients treated by each nurse in a specific specialization.
        
        num_pat = Nurse.objects.annotate(num = Count('patient'))
58. Find the patients who have been treated by more than one nurse.
        
        lucky_pat = Patient.objects.annotate(no_nurse = Count('nurse')).filter(no_nurse__lte=1)
59. Retrieve the names of doctors who have patients with a specific diagnosis and age group.
        
        Patient.objects.annotate(no_nurse = Count('nurse')).filter(no_nurse__gt=1)