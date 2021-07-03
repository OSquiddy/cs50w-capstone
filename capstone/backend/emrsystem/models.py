from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Doctor(models.Model):
    DoctorID = models.AutoField(primary_key=True)
    DOJ = models.DateField(auto_now_add=True)
    Phone_Number = models.CharField(max_length=15)
    
    UNIT1 = '01'
    UNIT2 = '02'
    unit_choices = [
        ('',''),
        (UNIT1, '01'),
        (UNIT2, '02')
    ]
    Unit = models.CharField(blank=True, max_length=2, choices=unit_choices)
    
    RADIOLOGY = 'rd'
    CARDIOLOGY = 'cd'
    DERMATOLOGY = 'dm'
    OBGYN = 'og'
    GASTROENTEROLOGY = 'gl'
    SURGERY = 'sg'
    HAEMATOLOGY = 'hm'
    ICU = 'ic'
    OTOLARYNGOLOGY = 'ot'
    PHYSIOTHERAPY = 'pt'
    department_choices = [
        ('',''),
        (RADIOLOGY, 'Radiology'),
        (CARDIOLOGY, 'Cardiology'),
        (DERMATOLOGY, 'Dermatology'),
        (GASTROENTEROLOGY, 'Gastroentrology'),
        (SURGERY, 'Surgery'),
        (OBGYN, 'Obstetrics & Gynecology'),
        (HAEMATOLOGY, 'Haematology'),
        (ICU, 'Intensice Care Unit'),
        (OTOLARYNGOLOGY, 'Otolaryngology'),
        (PHYSIOTHERAPY, 'Physiotherapy')
    ]
    Department = models.CharField(blank=True, null=True, max_length=2, choices=department_choices)
    
    INTERN = 'in'
    JUNIOR_RESIDENT = 'jr'
    SENIOR_RESIDENT = 'sr'
    ASSOCIATE_PROFESSOR = 'ap'
    ASSISTANT_PROFESSOR = 'as'
    PROFESSOR = 'pf'
    HOD = 'hd'
    role_choices = [
        ('', ''),
        (INTERN, 'Intern'),
        (JUNIOR_RESIDENT, 'Junior Resident'),
        (SENIOR_RESIDENT, 'Senior Resident'),
        (ASSOCIATE_PROFESSOR, 'Associate Professor'),
        (ASSISTANT_PROFESSOR, 'Assistant Professor'),
        (PROFESSOR, 'Professor'),
        (HOD, 'Head of Department (HOD)')
    ]
    Role = models.CharField(blank=True, null=True, max_length=2, choices=role_choices)
    
    def __str__(self):
        user = User.objects.get(DoctorID=self.DoctorID)
        return f"{user.first_name} {user.last_name}"
    
class Patient(models.Model):
    PatientID = models.AutoField(primary_key=True)
    # assigned_doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name='patients', null=True)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    fathers_name = models.CharField("Father's Name", null=True, max_length=50)
    mothers_name = models.CharField("Mother's Name", null=True, max_length=50)
    Phone_Number = models.CharField(null=True, max_length=15)
    occupation = models.CharField(null=True, max_length=55)
    
    # UNIT1 = '01'
    # UNIT2 = '02'
    # unit_choices = [
    #     ('',''),
    #     (UNIT1, '01'),
    #     (UNIT2, '02')
    # ]
    # Unit = models.CharField(blank=True, max_length=2, choices=unit_choices)
    
    IPD = 'ipd'
    OPD = 'opd'
    patientType_choices = [
        ('',''),
        (IPD, 'In-Patient Department'),
        (OPD, 'Out-Patient Department')
    ]
    patient_type = models.CharField(null=True, blank=True, max_length=3, choices=patientType_choices)
    
    sex_choices = [
        ('',''),
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ]
    sex = models.CharField(null=True, blank=True, max_length=1, choices=sex_choices)
    
    def __str__(self):
        user = User.objects.get(PatientID=self.PatientID)
        return f"{user.first_name} {user.last_name}"
    
class User(AbstractUser):

    DoctorID = models.OneToOneField(Doctor, on_delete=models.CASCADE, blank=True, null=True, related_name='doctorID')
    PatientID = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, null=True, related_name='patientID')

    def __str__(self):
        return f"{self.username}"
    
class Visit(models.Model):
    
    PatientID = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, null=True)
    visit_number = models.IntegerField(primary_key=True, serialize=True)
    date = models.DateField(auto_now_add=True)
    time_of_visit = models.TimeField(auto_now_add=True)
    payment = models.DecimalField(max_digits=20, decimal_places=2)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
      
    UNIT1 = '01'
    UNIT2 = '02'
    unit_choices = [
        ('',''),
        (UNIT1, '01'),
        (UNIT2, '02')
    ]
    Unit = models.CharField(blank=True, max_length=2, choices=unit_choices)
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=['PatientID', 'visit_number'], name='id') ]
        
    def __str__(self):
        return f"{self.PatientID} : {self.visit_number}"
    
class Examination(models.Model):
    visit_id = models.AutoField(primary_key=True)
    blood_pressure = models.CharField(max_length=10, blank=True, null=True)
    SpO2 = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pulse_rate = models.CharField(max_length=10, blank=True, null=True)
    general = models.TextField()
    respiratory = models.TextField()
    cardiovascular = models.TextField()
    cereberovascular = models.TextField()
    
    def __str__(self):
        return f"Examination for visit no. {self.visit_id} "