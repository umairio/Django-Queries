### Queries Part 2

1. Select all patients admitted after a specific date.

        Patient.objects.filter(date_admitted__gt = '2024-02-15')
2. Count the total number of patients.

        Patient.objects.count()
3. Count the total number of patients with a specific age.
        
        Patient.objects.filter(age = 22).count()
4. Select all patients with their associated doctors and nurses prefetched.
        
        Patient.objects.prefetch_related('doctor', 'nurse')
5. Count the total number of doctors associated with each patient.
        
        Patient.objects.annotate(num = Count('doctor')).values('name','num')
6. Sum the ages of all patients.
        
        age_sum = Patient.objects.aggregate(F(Sum('age')))
7. Select all patients along with the number of doctors associated with each.
        
        Patient.objects.values("name").annotate(docsum = Count('doctor'))
8. Select all patients along with their medical records, if available.
        
        Patient.objects.select_related('medical_record').values("name",'medical_record')
9. Count the total number of nurses associated with each patient.
        
        Patient.objects.annotate(nurs = Count('nurse')).values('name','nurs')
10. Select all patients with their associated nurses and the nurses' contact numbers.
        
        Patient.objects.select_related('nurse').values('name','nurse__name','nurse__contact_number')
11. Select all patients along with the total number of medical records for each.
        
        Patient.objects.annotate(nmr = Count('medical_record')).values('name','nmr')
12. Select all patients with their diagnoses and prescriptions, if available.

        Patient.objects.prefetch_related('medical_record').values("name",'medical_record__diagnoses','medical_record__prescription')
        MedicalRecord.objects.select_related('patient').values('patient__name',"diagnoses","prescription")
13. Count the total number of patients admitted in a specific year.
        
        Patient.objects.filter(date_admitted__)
15. Annotate the maximum age of patients.


16. Annotate the minimum age of patients.


17. Select all patients with their associated doctors and nurses.
        
        Patient.objects.values('name','doctor__name','nurse__name')
18. Select all patients along with the count of nurses they are associated with.

        Patient.objects.annotate(nurs = Count('nurse')).values('name','nurs')
19. Annotate the average age of patients.

        Patient.objects.annotate(avg_age = Avg('age'))
20. Select all patients along with the count of distinct doctors they are associated with.

        Patient.objects.select_related('doctor').distinct().annotate(num = Count('doctor')).values('name','num')
21. Select all doctors with their associated patients prefetched.

        Doctor.objects.prefetch_related('patient')
22. Select all nurses with their associated patients prefetched.

        Nurse.objects.prefetch_related('patient')
23. Select all patients along with the count of medical records for each.

        Patient.objects.annotate(num = Count('medical_record'))
24. Select all doctors with the count of patients they are associated with.

        Doctors.objects.annotate(num = Count('patient'))
25. Select all patients along with their doctors' specializations.

        Patient.objects.select_related('doctor').values('name','doctor__specialization')
26. Select all patients along with the earliest admission date.
        


