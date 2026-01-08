from django.conf import settings
from django.db import models
from django.utils import timezone
import random
STATUS = (
    ('','Select'),
    ('Approved','Approve'),
    ('Rejected', 'Reject'),)

class Area(models.Model):
	area_name=models.CharField(max_length=40,unique=True)
	def __str__(self):
		return self.area_name
class Hospital_Register(models.Model):
	hospital_name = models.CharField(max_length=40,unique=True)
	mail = models.EmailField(max_length=30)
	mobile = models.CharField(max_length=15)
	hospital_license_no = models.CharField(max_length=30,unique=True)
	username = models.CharField(max_length=40,unique=True)
	password = models.CharField(max_length=40)
	country = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	specialist = models.CharField(max_length=1000,blank=True,null=True)
	hospital_address = models.CharField(max_length=200)
	area =  models.ForeignKey(Area, on_delete=models.CASCADE)
	status =  models.CharField(max_length=200,choices=STATUS,blank=True,null=True)
	image = models.FileField('Upload Image',upload_to='documents/',null=True)
	def __str__(self):
		return self.hospital_name
class Customer_Detail(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	phone_number = models.CharField(max_length=30)
	country =  models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	username = models.CharField(max_length=30,unique=True)
	password =  models.CharField(max_length=30)
	def __str__(self):
		return self.name
class Facilities(models.Model):
	hospital_id =  models.ForeignKey(Hospital_Register, on_delete=models.CASCADE)
	doctor_detail = models.TextField(max_length=2000)
	bed_detail = models.IntegerField(null=True)
	blood_bank = models.TextField(max_length=2000)
	medical_detail = models.TextField(max_length=2000)
	ambulance = models.TextField(max_length=2000)
	other = models.TextField(max_length=2000)
	cylinder_count = models.IntegerField(null=True)
	def __str__(self):
		return self.hospital_id.hospital_name
