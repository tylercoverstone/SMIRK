# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#System Administrator Role
class System_Administrator(models.Model):
    Date = models.DateTimeField('Date')
    username = models.ForeignKey(User, blank=True, null=True)
    def __str__(self):
        return str(self.username)


#Doctor Role
class Doctor(models.Model):
    Practice_Name = models.CharField(max_length=200)
    Practice_Address = models.CharField(max_length=200)
    Recovery_Phrase = models.CharField(max_length=200)
    #Username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    username = models.ForeignKey(User, blank=True, null=True)
    #created_by = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return self.Practice_Name

#Nurse Role
class Nurse(models.Model):
    Practice_Name = models.CharField(max_length=200)
    Practice_Address = models.CharField(max_length=200)
    Associated_Doctors = models.ManyToManyField(Doctor)
    username = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return self.Practice_Name

#Medical Administrator Role
class Medical_Administrator(models.Model):
    Practice_Name = models.CharField(max_length=200)
    Practice_Address = models.CharField(max_length=200)
    Associated_Doctors = models.ManyToManyField(Doctor)
    Associated_Nurses = models.ManyToManyField(Nurse)
    username = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return self.Practice_Name

#Insurance Administrator Role
class Insurance_Administrator(models.Model):
    Company_Name = models.CharField(max_length=200)
    Company_Address = models.CharField(max_length=200)
    username = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return self.Company_Name

#Patient Role
class Patient(models.Model):
    SSN = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    DOB =  models.DateTimeField('Date')
    username = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return self.SSN

#Record
class Record(models.Model):
    Record_ID =  models.AutoField(primary_key=True)
    lst = ['Doctor Exam','Test Result','Diagnosis','Insurance Claim','Patient Doctor Correspondence','Raw']
    options = [(str(i), str(i)) for i in lst]
    Record_Type = models.CharField(max_length=200, choices=options, default='Doctor Exam')
    Record_Date =  models.DateTimeField('Record_Date', auto_now=True)
    Owner = models.ForeignKey(User, blank=True, null=True, related_name='Owner')
    Patient = models.ForeignKey(User, blank=True, null=True, related_name='Patient')
    Edit_Permissions = models.ManyToManyField(User, related_name='Edit_Permissions')
    View_Permissions = models.ManyToManyField(User, related_name='View_Permissions')
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.Record_ID)

#Doctor Exam Record
class Doctor_Exam_Record(models.Model):
    Date =  models.DateTimeField('Date of exam', auto_now=True)
    Doctor = models.ForeignKey(User, blank=True, null=True)
    Notes = models.CharField(max_length=200)
    Record = models.ForeignKey(Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)

#Diagnosis Record
class Diagnosis_Record(models.Model):
    Date =  models.DateTimeField('Date of exam', auto_now=True)
    Doctor = models.ForeignKey(User, blank=True, null=True)
    Diagnosis = models.CharField(max_length=200)
    Record = models.ForeignKey(Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)

#Test Results Record
class Test_Results_Record(models.Model):
    Date =  models.DateTimeField('Date of exam', auto_now=True)
    Doctor = models.ForeignKey(User, blank=True, null=True)
    Lab = models.CharField(max_length=200)
    Notes = models.CharField(max_length=200)
    Record = models.ForeignKey(Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)


#Insurance Claim Record
class Insurance_Claim_Record(models.Model):
    Date =  models.DateTimeField('Date of exam', auto_now=True)
    Medical_Administrator = models.ForeignKey(User, blank=True, null=True, related_name='Medical_Administrator_handling_claim_for_doctor')
    Amount = models.FloatField(default=0.0) # models.FloatField(null=True, blank=True, default=None)
    Status_Options = (('Filed', 'Filed'), ('Examining', 'Examining'),  ('Rejected', 'Rejected'),('Accepted', 'Accepted'), ( 'Paid', 'Paid'))
    Status = models.CharField(max_length=200, choices=Status_Options)
    Record = models.ForeignKey(Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)


#Patient_Doctor_Correspondence_Record
class Patient_Doctor_Correspondence_Record(models.Model):
    Doctor = models.ForeignKey(User, blank=True, null=True, related_name='Doctor')
    Notes = models.ManyToManyField('Note')
    Record = models.ForeignKey(Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)

#Raw Record
class Raw_Record(models.Model):
    Description = models.CharField(max_length=200)
    File = models.FileField(upload_to='documents')
    Record = models.ForeignKey(Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)

#Note
class Note(models.Model):
    Date =  models.DateTimeField('Note Date', auto_now=True)
    Text = models.CharField(max_length=200)
    Patient_Doctor_Correspondence = models.ForeignKey(Patient_Doctor_Correspondence_Record, blank=True, null=True)
    created_at = models.DateTimeField('Date', auto_now=True)
    def __str__(self):
        return str(self.id)

