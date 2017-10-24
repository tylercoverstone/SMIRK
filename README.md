# SMIRK
Secure Medical Information Repository Kit

This is a project I completed in a team with three other peers to compete in the University of Connecticut's annual CyberSEED 
cyber security hacking competition.

This program is a Django application which serves as a central source for record keeping in a hospital setting. Users 
authenticate themselves upon login and are assigned a corresponding role (i.e. Doctor, Patient, Medical Administrator, etc.).
With each role, a list of permissions are available to the user (i.e. view patients' information, create a certain type of 
record, view specific records, etc.).

The integration test client program can be run to insert test information to the application, and the status of the runtime
will be updated in the console as well as to be observable in the application.

The backdoor client is used to insert data from an XML file into the database, and can also be used to dump the database.

Tools Used:
- Python 2.6.3
- Django
- MariaDB
