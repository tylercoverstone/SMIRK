from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from smirk.models import *

from django.db import models
from django.contrib.auth.models import User, Group
from tastypie import fields

# Create your API endPoints here.

#User API
class User(ModelResource):
    #groups = fields.ToManyField(Group, 'groups', blank=True, null=True)
    class Meta:
	queryset = User.objects.all()
	resource_name = 'User'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Group API
class Group(ModelResource):
    class Meta:
	queryset = Group.objects.all()
	resource_name = 'Group'
        authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization() 
	
#System Administrator Role
class System_Administrator(ModelResource):
    username = fields.ToOneField(User, 'username', blank=True, null=True)
    class Meta:
	queryset = System_Administrator.objects.all()
	resource_name = 'System_Administrator'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization() 

#Doctor Role
class Doctor(ModelResource):
    username = fields.ToOneField(User, 'username', blank=True, null=True)
    class Meta:
	queryset = Doctor.objects.all()
	resource_name = 'Doctor'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization() 

#Nurse Role
class Nurse(ModelResource):
    username = fields.ToOneField(User, 'username', blank=True, null=True)
    Associated_Doctors = fields.ToManyField(Doctor, 'Associated_Doctors', blank=True, null=True)
    class Meta:
	queryset = Nurse.objects.all()
	resource_name = 'Nurse'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Medical Administrator Role
class Medical_Administrator(ModelResource):
    username = fields.ToOneField(User, 'username', blank=True, null=True)
    Associated_Doctors = fields.ToManyField(Doctor, 'Associated_Doctors', blank=True, null=True)
    Associated_Nurses = fields.ToManyField(Nurse, 'Associated_Nurses', blank=True, null=True)
    class Meta:
	queryset = Medical_Administrator.objects.all()
	resource_name = 'Medical_Administrator'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Insurance Administrator Role
class Insurance_Administrator(ModelResource):
    username = fields.ToOneField(User, 'username', blank=True, null=True)
    class Meta:
	queryset = Insurance_Administrator.objects.all()
	resource_name = 'Insurance_Administrator'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Patient Role
class Patient(ModelResource):
    username = fields.ToOneField(User, 'username', blank=True, null=True)
    class Meta:
	queryset = Patient.objects.all()
	resource_name = 'Patient'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Record
class Record(ModelResource):
    Owner = fields.ToOneField(User, 'Owner', blank=True, null=True)
    Patient = fields.ToOneField(User, 'Patient', blank=True, null=True)
    class Meta:
	queryset = Record.objects.all()
	resource_name = 'Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Doctor Exam Record
class Doctor_Exam_Record(ModelResource):
    Doctor = fields.ToOneField(User, 'Doctor', blank=True, null=True)
    Record = fields.ToOneField(Record, 'Record', blank=True, null=True)
    class Meta:
	queryset = Doctor_Exam_Record.objects.all()
	resource_name = 'Doctor_Exam_Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Diagnosis Record
class Diagnosis_Record(ModelResource):
    Doctor = fields.ToOneField(User, 'Doctor', blank=True, null=True)
    Record = fields.ToOneField(Record, 'Record', blank=True, null=True)
    class Meta:
	queryset = Diagnosis_Record.objects.all()
	resource_name = 'Diagnosis_Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Test Results Record
class Test_Results_Record(ModelResource):
   Doctor = fields.ToOneField(User, 'Doctor', blank=True, null=True)
   Record = fields.ToOneField(Record, 'Record', blank=True, null=True)
   class Meta:
	queryset = Test_Results_Record.objects.all()
	resource_name = 'Test_Results_Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization() 

#Insurance Claim Record
class Insurance_Claim_Record(ModelResource):
   Medical_Administrator = fields.ToOneField(User, 'Medical_Administrator', blank=True, null=True)
   Record = fields.ToOneField(Record, 'Record', blank=True, null=True)
   class Meta:
	queryset = Insurance_Claim_Record.objects.all()
	resource_name = 'Insurance_Claim_Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization() 

#Patient_Doctor_Correspondence_Record
class Patient_Doctor_Correspondence_Record(ModelResource):
    Doctor = fields.ToOneField(User, 'Doctor', blank=True, null=True)
    Record = fields.ToOneField(Record, 'Record', blank=True, null=True)
    class Meta:
	queryset = Patient_Doctor_Correspondence_Record.objects.all()
	resource_name = 'Patient_Doctor_Correspondence_Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Raw Record
class Raw_Record(ModelResource):
    Record = fields.ToOneField(Record, 'Record', blank=True, null=True)
    class Meta:
	queryset = Raw_Record.objects.all()
	resource_name = 'Raw_Record'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
	
#Note
class Note(ModelResource):
    Patient_Doctor_Correspondence = fields.ToOneField(Patient_Doctor_Correspondence_Record, 'Patient_Doctor_Correspondence_Record', blank=True, null=True)
    class Meta:
	queryset = Note.objects.all()
	resource_name = 'Note'
	authentication = BasicAuthentication() #Authentication()
	authorization = DjangoAuthorization() #Authorization()
