import requests
import json

base_url = 'http://127.0.0.1:8000/api/'
auth = ('Admin', 'LetMeIn@UNF')

def insert(payload, service):
    url = base_url + service
    #payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False, auth=auth)
    #print(response)
    location = response.headers['Location']
    #print(location)
    return location

def g(resource_uri):
    response = requests.get("http://127.0.0.1:8000/" + resource_uri, auth=auth)
    data = response.json()
    return data
    #print (data)
    #print data['id']
#

### INTEGRATION TEST SCENARIOS ###

#Test Sequence #1: /setITAdmin function
payload = {"first_name": "Dade", "is_staff": True, "last_name": "Murphy", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "DMurphy", "groups" : ["/api/Group/2/",]}

User_DMurphy = insert(payload, "User/")


#Test Sequence #2: /createDoctor
payload = {"first_name": "Kate", "is_staff": True, "last_name": "Libby", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "KLibby", "groups" : ["/api/Group/3/",]}

User_KLibby = insert(payload, "User/")

payload = {"Practice_Address": "1995 Aburn Road, Chicago IL 60007", "Practice_Name": "The Gibson Associates","Recovery_Phrase": "You are not in my class", "username": User_KLibby}
Doctor_KLibby = insert(payload, "Doctor/")



#Test Sequence #3: /createPatient
payload = {"first_name": "Martin", "is_staff": True, "last_name": "Bishop", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "MBishop", "groups" : ["/api/Group/1/",]}

User_MBishop = insert(payload, "User/")

payload = {"Address": "145 Redford Drive, Baltimore, MD 21234", "DOB": "1936-08-18T00:00:00", "SSN": "312-12-4253", "username": User_MBishop}
Patient_MBishop = insert(payload, "Patient/")



#Test Sequence #4: /addDoctorExamRecord
payload = {"Record_ID": 9123245, "Owner": User_KLibby, "Patient": User_MBishop, "Record_Type": "Doctor Exam"}
Record_uri = insert(payload, "Record/")

payload = {"Doctor": User_KLibby, "Notes": "Looks great for his age", "Record": Record_uri}
Doctor_Exam_Record_uri = insert(payload, "Doctor_Exam_Record/")

#Test Sequence #5: /listRecords
data = g('api/Record/')
for x in data['objects']:
    print(x['Record_ID'])

#Test Sequence #6: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 9123245):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))


#Test Sequence #7: /viewRecoveryPhrase
response = requests.get("http://127.0.0.1:8000" + Doctor_KLibby, auth=auth)
data = response.json()
print data['Recovery_Phrase']

#Test Sequence #8: /addDiagnosisRecord
payload = {"Record_ID": 832942, "Owner": User_KLibby, "Patient": User_MBishop, "Record_Type": "Diagnosis"}
Record_uri2 = insert(payload, "Record/")

payload = {"Doctor": User_KLibby, "Diagnosis": "Positive for The Sting", "Record": Record_uri2}
Diagnosis_Record_uri = insert(payload, "Diagnosis_Record/")

#Test Sequence #9: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 832942):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #10: /createNurse
payload = {"first_name": "Kevin", "is_staff": True, "last_name": "Flynn", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "KFlynn", "groups" : ["/api/Group/4/",]}

User_KFlynn = insert(payload, "User/")

payload = {"Practice_Address": "1983 Aburn Road, Chicago IL 60007", "Practice_Name": "The Gibson Associates","Associated_Doctors": [Doctor_KLibby,], "username": User_KFlynn}
Nurse_KFlynn = insert(payload, "Nurse/")


#Test Sequence #11: /createMedAdmin
payload = {"first_name": "David", "is_staff": True, "last_name": "Lightman", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "DLightman", "groups" : ["/api/Group/6/",]}

User_DLightman = insert(payload, "User/")

payload = {"username": User_DLightman, "Practice_Address": "1983 Aburn Road, Chicago IL 60007", "Practice_Name": "The Gibson Associates", "Associated_Doctors": [Doctor_KLibby,], "Associated_Nurses": [Nurse_KFlynn,]}
Medical_Administrator_DLightman = insert(payload, "Medical_Administrator/")

#Test Sequence #12: /viewPatient
data = g('api/Patient/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["username"] == User_MBishop):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #13: /addTestResultRecord
payload = {"Record_ID": 5434567, "Owner": User_KFlynn, "Patient": User_MBishop, "Record_Type": "Test Result"}
Record_uri3 = insert(payload, "Record/")

payload = {"Doctor": User_KLibby, "Lab": "ENCOM", "Notes": "Digitizing", "Record": Record_uri3}
Test_Results_Record_uri = insert(payload, "Test_Results_Record/")

#Test Sequence #14: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 5434567):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #15: /createInsAdmin
payload = {"first_name": "Penelope", "is_staff": True, "last_name": "Garcia", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "PGarcia", "groups" : ["/api/Group/5/",]}

User_PGarcia = insert(payload, "User/")

payload = {"username": User_PGarcia, "Company_Address": "17000 Denechi Rd, Austin, TX 73301", "Company_Name": "Vangsness Insurance"}
Insurance_Administrator_DLightman = insert(payload, "Insurance_Administrator/")

#Test Sequence #16: /addInsClaimRecord
payload = {"Record_ID": 2114563, "Owner": User_PGarcia, "Patient": User_MBishop, "Record_Type": "Insurance Claim"}
Record_uri4 = insert(payload, "Record/")

payload = {"Medical_Administrator": User_DLightman, "Status": "Filed", "Amount": "745.00", "Record": Record_uri4}
Insurance_Claim_Record_uri = insert(payload, "Insurance_Claim_Record/")

#Test Sequence #17: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 832942):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #18: /addCorrespondenceRecord
payload = {"Record_ID": 7753571, "Owner": User_KLibby, "Patient": User_MBishop, "Record_Type": "Patient Doctor Correspondence"}
Record_uri5 = insert(payload, "Record/")

payload = {"Doctor": User_KLibby, "Notes": "", "Record": Record_uri5}
Correspondence_Record_uri = insert(payload, "Patient_Doctor_Correspondence_Record/")

#Test Sequence #19: /addNote
payload = {"Date": "8/14/2017", "Notes": "Change bandage daily.", "Patient_Doctor_Correspondence_Record": Correspondence_Record_uri}
Note1_uri = insert(payload, "Note/")

#Test Sequence #20: /addNote
payload = {"Date": "8/15/2017", "Notes": "Does this look infected?", "Patient_Doctor_Correspondence_Record": Correspondence_Record_uri}
Note1_uri = insert(payload, "Note/")

#Test Sequence #21: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 7753571):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #22: /addRawRecord
payload = {"Record_ID": 63481249, "Owner": User_PGarcia, "Patient": User_MBishop, "Record_Type": "Raw"}
Record_uri6 = insert(payload, "Record/")

payload = {"Description": "License Scan", "File": "TWFulGlzIGRpc3RpbmdlaXNoZWQsIG5vdCBvbmx", "Record": Record_uri6}
Raw_Record_uri = insert(payload, "Raw_Record/")

#Test Sequence #23: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 63481249):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #24: /editRecordPermissions

#Test Sequence #25: /viewRecord
data = g('api/Record/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["Record_ID"] == 63481249):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

#Test Sequence #26: /editRecordPermissions

#Test Sequence #27: /editPatient
data = g('api/Patient/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["username"] == User_MBishop):
        d["DOB"] = "9/1/78"

#Test Sequence #28: /viewPatient
data = g('api/Patient/')
for x in range(len(data['objects'])):
    d = data['objects'][x]
    if(d["username"] == User_MBishop):
        for key,value in d.iteritems():
            print("{0} : {1}".format(key, value))

