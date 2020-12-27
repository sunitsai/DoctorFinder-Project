from django.db import models

# Create your models here.

class User(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    Otp = models.CharField(max_length=50)
    is_create = models.DateTimeField(auto_now_add=True)
    is_update = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class Doctor(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100, blank= True)
    Contact = models.BigIntegerField(default=122)
    Year_of_experience = models.IntegerField(default=2)
    Clinic_name = models.CharField(max_length=50)
    Specialazion = models.CharField(max_length=50)
    address = models.CharField(max_length= 500,blank = True)
    city = models.CharField(max_length = 50,default="")
    state = models.CharField(max_length =50, blank= True)
    Gender = models.CharField(max_length=10,default="")
    birthdate = models.DateField(blank=True,default="2020-06-27")
    location = models.CharField(max_length= 30,blank= True)
    about_doc = models.CharField(max_length= 100,blank= True)
    profile_pic=models.FileField(upload_to='doctorfinder/img/',default='doc_male.png')

class Patient(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.BigIntegerField(default=122)
    Address = models.CharField(max_length=100)
    Gender = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True)
    birthdate = models.DateField(blank=True,default="2020-06-27")

    #updated patiend profile

    blood_group=models.CharField(max_length=10,blank= True)
    blood_presure=models.CharField(max_length=10,blank= True)
    sugar=models.CharField(max_length=10,blank= True)
    Haemoglobin=models.CharField(max_length=10,blank= True)
    profile_pic=models.FileField(upload_to='doctorfinder/img/',default='patient_icon.png')

class Pharmacy(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.BigIntegerField(default=122)
    Address = models.CharField(max_length=50)
    Drug_name = models.CharField(max_length=50)
    Prescription = models.CharField(max_length=50)
    Gender = models.CharField(max_length=20)

class Case(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    disease = models.CharField(max_length = 100)
    symptoms = models.CharField(max_length = 200)
    status = models.BooleanField(default= False)

class availability(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    avail_date = models.DateField()
    start_time = models.CharField(max_length = 100)
    status = models.BooleanField(default= False)


class Appointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete = models.CASCADE)
    availability_id = models.ForeignKey(availability, on_delete = models.CASCADE,default = None)
    appointment_status = models.BooleanField(default= False)
    payment_status = models.BooleanField(default= False)


class Prescription(models.Model):
    case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    attachment_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True,blank=False)


class Payment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=300)