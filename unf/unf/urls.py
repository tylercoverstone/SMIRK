"""unf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from smirk.resources import *

urlpatterns = [
        url(r'^', admin.site.urls),
	url(r'^createPatient', RedirectView.as_view(url='smirk/patient/add/', permanent=True), name="createPatient"),
	url(r'^createDoctor', RedirectView.as_view(url='smirk/doctor/add/', permanent=False)),
	url(r'^createNurse', RedirectView.as_view(url='smirk/nurse/add/', permanent=False)),
	url(r'^createSysAdmin', RedirectView.as_view(url='smirk/system_administrator/add/', permanent=False)),
	url(r'^createMedAdmin', RedirectView.as_view(url='smirk/medical_administrator/add/', permanent=False)),
	url(r'^createInsAdmin', RedirectView.as_view(url='smirk/insurance_administrator/add/', permanent=False)),
	url(r'^editPerm', RedirectView.as_view(url='auth/group/', permanent=False)),
	url(r'^addDoctorExamRecord', RedirectView.as_view(url='smirk/doctor_exam_record/add/', permanent=False)),
	url(r'^addTestResultRecord', RedirectView.as_view(url='smirk/test_results_record/add/', permanent=False)),
	url(r'^addDiagnosisRecord', RedirectView.as_view(url='smirk/diagnosis_record/add/', permanent=False)),
	url(r'^addInsuranceClaimRecord', RedirectView.as_view(url='smirk/insurance_claim_record/add/', permanent=False)),
	url(r'^addRawRecord', RedirectView.as_view(url='smirk/raw_record/add/', permanent=False)),
	url(r'^createCorrespondenceRecord', RedirectView.as_view(url='smirk/patient_doctor_correspondence_record/add/', permanent=False)),
	url(r'^addCorrespondenceNote', RedirectView.as_view(url='smirk/note/add/', permanent=False)),
	url(r'^listRecords', RedirectView.as_view(url='smirk/record/', permanent=False)),
	url(r'^viewRecord',  RedirectView.as_view(url='smirk/record/', permanent=False)),
	url(r'^editRecordPerm', RedirectView.as_view(url='auth/group/', permanent=False)),
	url(r'^editPatient', RedirectView.as_view(url='smirk/patient/', permanent=False)),
	url(r'^editDoctor', RedirectView.as_view(url='smirk/doctor/', permanent=False)),
	url(r'^editNurse', RedirectView.as_view(url='smirk/nurse/', permanent=False)),
	url(r'^editSysAdmin', RedirectView.as_view(url='smirk/system_administrator/', permanent=False)),
	url(r'^editMedAdmin', RedirectView.as_view(url='smirk/medical_administrator/', permanent=False)),
	url(r'^editInsAdmin', RedirectView.as_view(url='smirk/insurance_administrator/', permanent=False)),
	url(r'^viewPatientProfile', RedirectView.as_view(url='smirk/patient/', permanent=False)),
	url(r'^viewRecoveryPhrase', RedirectView.as_view(url='smirk/doctor/', permanent=False)),
	url(r'^removeUserProfile', RedirectView.as_view(url='auth/user/', permanent=False)),
	url(r'^api/', include(System_Administrator().urls)),
	url(r'^api/', include(Doctor().urls)),
	url(r'^api/', include(Nurse().urls)),
	url(r'^api/', include(Medical_Administrator().urls)),
	url(r'^api/', include(Insurance_Administrator().urls)),
	url(r'^api/', include(Patient().urls)),
	url(r'^api/', include(Record().urls)),
	url(r'^api/', include(Doctor_Exam_Record().urls)),
	url(r'^api/', include(Diagnosis_Record().urls)),
	url(r'^api/', include(Test_Results_Record().urls)),
	url(r'^api/', include(Insurance_Claim_Record().urls)),
	url(r'^api/', include(Patient_Doctor_Correspondence_Record().urls)),
	url(r'^api/', include(Raw_Record().urls)),
	url(r'^api/', include(Note().urls)),
        url(r'^api/', include(User().urls)),
        url(r'^api/', include(Group().urls)),
]

admin.site.site_header= 'Secure Medical Information Repository Kit'
admin.site.index_title= 'SMIRK'
admin.site.site_title= 'Welcome' 


