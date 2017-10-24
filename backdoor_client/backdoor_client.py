import requests
import json
import sys
import xml
from xml.dom import minidom
import xml.etree.ElementTree as ET

base_url = 'http://127.0.0.1:8000/api/'
server_url = "http://127.0.0.1:8000/"
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
    response = requests.get(server_url + resource_uri, auth=auth)
    data = response.json()
    return data
    #print (data)
    #print data['id']
#

def loadXML(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    print root.tag
    print root.attrib
    
    for child in root:
        if child.tag == "SystemAdministratorUserProfile":
            
            payload = {"first_name": child[2].text, "is_staff": True, "last_name": child[3].text, "password": "3e06434338085d2ddf6ddcde204101f0", "username":  child[0].text, "auth_group" : ["/api/Group/2/",]}
            User_DMurphy = insert(payload, "User/")

        elif child.tag == "DoctorUserProfile":
            payload = {"first_name": child[2].text, "is_staff": True, "last_name": child[3].text, "password": "3e06434338085d2ddf6ddcde204101f0", "username": child[0].text, "auth_group" : ["/api/Group/3/",]}

            User_KLibby = insert(payload, "User/")

            payload = {"Practice_Address": child[5].text, "Practice_Name": child[4].text,"Recovery_Phrase": child[6].text, "username": User_KLibby}

            Doctor_KLibby = insert(payload, "Doctor/")

        elif child.tag == "PatientUserProfile":
            payload = {"first_name": child[2].text, "is_staff": True, "last_name": child[3].text, "password": "3e06434338085d2ddf6ddcde204101f0", "username": child[0].text, "auth_group" : ["/api/Group/1/",]}

            User_MBishop = insert(payload, "User/")

            payload = {"Address": child[6].text, "DOB": child[4].text, "SSN": child[5].text, "username": User_MBishop}

            Patient_MBishop = insert(payload, "Patient/")

        elif child.tag == "NurseUserProfile":
            payload = {"first_name": child[2].text, "is_staff": True, "last_name": child[3].text, "password": "3e06434338085d2ddf6ddcde204101f0", "username": child[0].text, "auth_group" : ["/api/Group/4/",]}
        
            User_KFlynn = insert(payload, "User/")
            
            temp1 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[6].text):
                    temp1 = d["resource_uri"]
        
            temp2 = ""
            
            data = g('api/Doctor/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == temp1):
                    temp2 = d["resource_uri"]


            payload = {"Practice_Address": child[5].text, "Practice_Name": child[4].text,"Associated_Doctors": [temp2,], "username": User_KFlynn}
            
            Nurse_KFlynn = insert(payload, "Nurse/")
                
        elif child.tag == "MedicalAdministratorUserProfile":
            payload = {"first_name": child[2].text, "is_staff": True, "last_name": child[3].text, "password": "3e06434338085d2ddf6ddcde204101f0", "username": child[0].text, "auth_group" : ["/api/Group/5/",]}
        
            User_DLightman = insert(payload, "User/")
            
            temp1 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[6].text):
                    temp1 = d["resource_uri"]

            temp2 = ""

            data = g('api/Doctor/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == temp1):
                    temp2 = d["resource_uri"]

            temp3 = ""
    
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[7].text):
                    temp3 = d["resource_uri"]
    
            temp4 = ""
            
            data = g('api/Nurse/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == temp3):
                    temp4 = d["resource_uri"]
    
    
            payload = {"Practice_Address": child[5].text, "Practice_Name": child[4].text,"Associated_Doctors": [temp2,], "Associated_Nurses": [temp4,], "username": User_DLightman}
            
            Med_Admin_DLightman = insert(payload, "Medical_Administrator/")
                
        elif child.tag == "InsuranceAdministratorUserProfile":
            payload = {"first_name": child[2].text, "is_staff": True, "last_name": child[3].text, "password": "3e06434338085d2ddf6ddcde204101f0", "username": child[0].text, "auth_group" : ["/api/Group/6/",]}
    
            User_PGarcia = insert(payload, "User/")

            payload = {"Company_Address": child[5].text, "Company_Name": child[4].text, "username": User_PGarcia}
    
            Ins_Admin_PGarcia = insert(payload, "Insurance_Administrator/")
        
        elif child.tag == "DoctorExamRecord":
            
            temp1 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[3].text):
                    temp1 = d["resource_uri"]

            temp2 = ""
    
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[4].text):
                    temp2 = d["resource_uri"]
    
            temp3 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[8].text):
                    temp3 = d["resource_uri"]

            editPermissions = child[5].text.split(',')

            viewPermissions = child[6].text.split(',')

            for person in range(len(editPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]

            for person in range(len(viewPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]


            payload = {"Record_ID": child[0].text, "Owner": temp1, "Patient": temp2, "Record_Type": child[1].text[:-7], "View_Permissions": viewPermissions, "Edit_Permissions": editPermissions, "Record_Date": child[2].text}
    
            Record_uri = insert(payload, "Record/")

            payload = {"Date": child[7].text, "Doctor": temp3, "Notes": child[9].text, "Record": Record_uri}
            
            Doctor_Exam_Record_uri = insert(payload, "Doctor_Exam_Record/")
                
        elif child.tag == "DiagnosisRecord":

            temp1 = ""
    
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[3].text):
                    temp1 = d["resource_uri"]
    
            temp2 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[4].text):
                    temp2 = d["resource_uri"]
        
            temp3 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[8].text):
                    temp3 = d["resource_uri"]

            editPermissions = child[5].text.split(',')
    
            viewPermissions = child[6].text.split(',')
        
            for person in range(len(editPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]
    
            for person in range(len(viewPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]
        
        
            payload = {"Record_ID": child[0].text, "Owner": temp1, "Patient": temp2, "Record_Type": child[1].text[:-7], "View_Permissions": viewPermissions, "Edit_Permissions": editPermissions, "Record_Date": child[2].text}
            
            Record_uri = insert(payload, "Record/")
            
            payload = {"Date": child[7].text, "Doctor": temp3, "Diagnosis": child[9].text, "Record": Record_uri}
            
            Diagnosis_Record_uri = insert(payload, "Diagnosis_Record/")
                
        elif child.tag == "TestResultsRecord":

            temp1 = ""
    
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[3].text):
                    temp1 = d["resource_uri"]
    
            temp2 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[4].text):
                    temp2 = d["resource_uri"]
        
            temp3 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[8].text):
                    temp3 = d["resource_uri"]

            editPermissions = child[5].text.split(',')
            
            viewPermissions = child[6].text.split(',')
            
            for person in range(len(editPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]

            for person in range(len(viewPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]
        
        
            payload = {"Record_ID": child[0].text, "Owner": temp1, "Patient": temp2, "Record_Type": child[1].text[:-7], "View_Permissions": viewPermissions, "Edit_Permissions": editPermissions, "Record_Date": child[2].text}
            
            Record_uri = insert(payload, "Record/")
            
            payload = {"Date": child[7].text, "Doctor": temp3, "Lab": child[9].text, "Notes": child[10].text,"Record": Record_uri}
    
            Test_Results_Record_uri = insert(payload, "Test_Results_Record/")
                
        elif child.tag == "InsuranceClaimRecord":

            temp1 = ""
    
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[3].text):
                    temp1 = d["resource_uri"]
    
            temp2 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[4].text):
                    temp2 = d["resource_uri"]
        
            temp3 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[8].text):
                    temp3 = d["resource_uri"]

            editPermissions = child[5].text.split(',')
            
            viewPermissions = child[6].text.split(',')
            
            for person in range(len(editPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]

            for person in range(len(viewPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]
        
        
            payload = {"Record_ID": child[0].text, "Owner": temp1, "Patient": temp2, "Record_Type": child[1].text[:-7], "View_Permissions": viewPermissions, "Edit_Permissions": editPermissions, "Record_Date": child[2].text}
            
            Record_uri = insert(payload, "Record/")
            
            payload = {"Date": child[7].text, "Medical_Administrator": temp3, "Amount": child[9].text, "Status": child[10].text,"Record": Record_uri}
    
            Insurance_Record_uri = insert(payload, "Insurance_Claim_Record/")


        elif child.tag == "PatientDoctorCorrespondenceRecord":
    
            temp1 = ""
        
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[3].text):
                    temp1 = d["resource_uri"]
    
            temp2 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[4].text):
                    temp2 = d["resource_uri"]
        
            editPermissions = child[5].text.split(',')
            
            viewPermissions = child[6].text.split(',')
            
            for person in range(len(editPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]

            for person in range(len(viewPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]

            temp3 = ""
    
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[7].text):
                    temp3 = d["resource_uri"]

            notes = []
            finalNotes = []

            if ET.iselement(child[8]):
                notes = child[8].getchildren()
                for note in notes:
                    children = note.getchildren()
                    payload = {"Date": children[0].text, "Text": children[1].text}
                    Note_uri = insert(payload, "Note/")
                    finalNotes.append(Note_uri)

            payload = {"Record_ID": child[0].text, "Owner": temp1, "Patient": temp2, "Record_Type": child[1].text[:-7], "View_Permissions": viewPermissions, "Edit_Permissions": editPermissions, "Record_Date": child[2].text}
    
            Record_uri = insert(payload, "Record/")
        
            payload = {"Doctor": temp3, "Record": Record_uri, "Notes": finalNotes}
            
            PCDC_Record_uri = insert(payload, "Patient_Doctor_Correspondence_Record/")


        elif child.tag == "RawRecord":
    
            temp1 = ""
        
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[3].text):
                    temp1 = d["resource_uri"]
    
            temp2 = ""
            
            data = g('api/User/')
            for x in range(len(data['objects'])):
                d = data['objects'][x]
                if(d["username"] == child[4].text):
                    temp2 = d["resource_uri"]

            editPermissions = child[5].text.split(',')
            
            viewPermissions = child[6].text.split(',')
            
            for person in range(len(editPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]

            for person in range(len(viewPermissions)):
                data = g('api/User/')
                for x in range(len(data['objects'])):
                    d = data['objects'][x]
                    if(d["username"] == person):
                        person = d["resource_uri"]
        
        
            payload = {"Record_ID": child[0].text, "Owner": temp1, "Patient": temp2, "Record_Type": child[1].text[:-7], "View_Permissions": viewPermissions, "Edit_Permissions": editPermissions, "Record_Date": child[2].text}
            
            Record_uri = insert(payload, "Record/")
            
            payload = {"Description": child[7].text, "File": child[8].text, "Record": Record_uri}
    
            Raw_Record_uri = insert(payload, "Raw_Record/")

def loadBackupCfg(cfgFile):
    file = open(cfgFile, "w+")
    file.write("offsite-server-ip = 172.17.0.2\n")
    file.write("offsite-server-username = root\n")
    file.write("offsite-server-password = appsec\n")
    file.close()
    
def getBackupCfg():
    try:
        file = open("db_backup_2017.cfg", "r")
        for line in file:
            print line
    except IOError:
        print "No cfg loaded"


    #
    #child.attrib
    #print child.text
        #

    """
    xmldoc = minidom.parse(xmlFile)
    
    itemlist = xmldoc.getElementsByTagName('SystemAdministratorUserProfile')
    print(len(itemlist))

    for s in itemlist:
        print s.childNodes[0].nodeValue
    #print '' .join([node.data for node in s.childNodes])
    #print(s.getElementsByTagName('Username')[0].c)

        """

### INTEGRATION TEST SCENARIOS ###


s = sys.argv[1]

if s == "setITAdmin":
    payload = {"first_name": "Tyler", "is_staff": True, "last_name": "Coverstone", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "UNF", "groups" : ["/api/Group/2/",]}
    User_UNF = insert(payload, "User/")

elif s == "loadData":
    xmlFile = sys.argv[2]
    loadXML(xmlFile)

elif s == "loadBackupCfg":
    cfgFile = sys.argv[2]
    loadBackupCfg(cfgFile)

elif s == "getBackupCfg":
    getBackupCfg()

elif s == "mysqldump":
    print "sudo mysqldump -X SMIRK > smirkDBDump.xml"
    print "DB Dump are saved into file smirkDBDump.xml"
