from django.contrib.auth.models import AbstractUser
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db.models.fields.related import OneToOneField
from django.core.files.storage import FileSystemStorage

# Functions that a model can use
def calc_visit(patient):
    prev_visits = Visit.objects.filter(patient=patient).order_by('-visit_number').values_list('visit_number', flat=True)
    if prev_visits:
        return prev_visits[0] + 1
    else:
        return 1

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name

def new_filename(instance, filename):
        basename, extension = filename.split('.')
        return f"{instance.id}_{instance.username}.{extension}"

# def check_validity(visit):
#     prev_visit = Visit.objects.filter(patient=visit.patient).order_by('-visit_number')
#     return visit.date < prev_visit.date


# Create your models here.
class MyBaseUser(AbstractUser):
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    Phone_Number = models.CharField(null=True, max_length=15)
    address = models.TextField(null=True)
    date_of_birth = models.DateField(null=True)
    isDoctor = models.BooleanField(null=True)
    isPatient = models.BooleanField(null=True)
    profilePic = models.ImageField(upload_to=new_filename, storage=OverwriteStorage(), null=True, blank=True)
    sex_choices = [
        ('',''),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    sex = models.CharField(null=True, blank=True, max_length=1, choices=sex_choices)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def geProfileUrl(self):
        if self.profilePic and hasattr(self.profilePic, 'url'):
            return self.profilePic.url
        else:
            pass
            # return "/static/network/images/defaultAvatar.png"

    def __str__(self):
        return f"{self.username}"

class Doctor(MyBaseUser):
    # mybaseuser_ptr = OneToOneField(MyBaseUser, on_delete=models.CASCADE, null=True, blank=True)
    DOJ = models.DateField(auto_now_add=True)
    
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
    
    class Meta:
        verbose_name="doctor"
        verbose_name_plural="doctors"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Patient(MyBaseUser):
    age = models.IntegerField(null=True)
    fathers_name = models.CharField("Father's Name", null=True, max_length=50)
    mothers_name = models.CharField("Mother's Name", null=True, max_length=50)
    occupation = models.CharField(null=True, max_length=55)
    blood_type = models.CharField(max_length=5, null=True, blank=True)
    last_visit = models.DateField(null=True, blank=True)
    
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
    
    class Meta:
        verbose_name="patient"
        verbose_name_plural="patients"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True, related_name="visits")
    visit_number = models.PositiveIntegerField()
    date = models.DateField()
    time_from = models.TimeField()
    time_till = models.TimeField()
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
    visit_completed = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'visit_number'], name='Visit Number')
        ]

    def save(self, *args, **kwargs):
        if self.visit_number is None:
            visit_number = calc_visit(self.patient)
            print('New visit no. is :', visit_number)
            self.visit_number = visit_number
        super(Visit, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.patient}: Visit {self.visit_number}"
    
class Examination(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, null=True, blank=True, related_name='examinations')
    blood_pressure = models.CharField(max_length=10, blank=True, null=True)
    SpO2 = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pulse_rate = models.CharField(max_length=10, blank=True, null=True)
    respiratory = models.TextField(default='NAD')
    cardiovascular = models.TextField(default='NAD')
    cereberovascular = models.TextField(default='NAD')
    per_abdominal = models.TextField(default='NAD')
    local_examination = models.TextField(default='NAD')
    others = models.TextField(null=True)
    complaints = models.TextField()
    diagnosis = models.TextField()
    pallor = models.BooleanField(default=False)
    clubbing = models.BooleanField(default=False)
    lymphadenopathy = models.BooleanField(default=False)
    icterus = models.BooleanField(default=False)
    koilonychia = models.BooleanField(default=False)
    oedema = models.BooleanField(default=False)
    
    def __str__(self):

        return f"Examination for {self.visit}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['visit'], name='Examination Number')
        ]

class PastHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, related_name='past_histories')
    surgeries = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    general = models.TextField(null=True, blank=True)
    drugs = models.TextField(null=True, blank=True)
    family = models.TextField(null=True, blank=True)
    t2dm = models.BooleanField(default=False, null=True)
    heart_disease = models.BooleanField(default=False, null=True)
    hypothyroidism = models.BooleanField(default=False, null=True)
    chronic_kidney_disease = models.BooleanField(default=False, null=True)
    cardiovascular_disease = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name="Past History"
        verbose_name_plural="Past History"
    
    def __str__(self):
        return f"Past History for {self.patient}"
    
class GynecHistory(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, null=True, blank=True, related_name='gynec_histories')
    gplad = models.CharField(max_length=10, blank=True, null=True)
    edd = models.DateField(null=True, blank=True)
    lmp = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name="Gynec History"
        verbose_name_plural="Gynec History"

    def __str__(self):
        return f"Past History for {self.visit}"