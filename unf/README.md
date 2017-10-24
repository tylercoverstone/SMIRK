# unf

Please follow these steps to set the application [Ubuntu]:

1. login to MariaDB using username root and password appsec
mysql -u root -p

2. create database called SMIRK 
CREATE DATABASE SMIRK; exit;

3. download git repository
git clone https://github.com/this-is-for-a-team/unf.git


4. install libraries
sudo apt-get update; 
sudo apt-get install libmysqlclient-dev python-dev;
sudo pip install django-tastypie django mysqlclient;

5. run server
cd unf; 
python manage.py migrate; 
python manage.py loaddata fixtures/initial_data.json;
sudo python manage.py runserver

note: to run the server on port 80, do these
sudo service nginx stop; #skip this
sudo python manage.py runserver 80