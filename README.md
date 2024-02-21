# cs415_project
Project for CS415 semester

Creating a website using virtual machines as the backend for a semester project

EC2 Initialization Script

#!/bin/bash
sudo apt update -y
sudo apt install ruby wget -y
cd /home/ubuntu
sudo wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto
sudo apt-get install python3-pip -y
sudo apt install python3.10-venv -y
sudo apt-get install python3-dev -y
sudo apt-get install default-libmysqlclient-dev -y
sudo apt-get install build-essential -y
sudo mkdir -pv /var/{log,run}/gunicorn/
sudo chown -cR ubuntu:ubuntu /var/{log,run}/gunicorn/



sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3




sudo apt install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2


Ubuntu:
Change mysqlclient to 2.1.1 in requirements.txt
push to repo
CodeDeploy to Instance
sudo apt-get install python3-pip -y
    - <tab> CLick OK
sudo apt install python3.10-venv -y
    - select all (space bar and arrow) and click OK
sudo python3 -m venv env
source env/bin/activate
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y
    - tab then Ok

sudo pip install mysqlclient==2.1.1
sudo pip install -r requirements.txt
sudo pip install gunicorn



Mysql Client
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install mysqlclient

start server
sudo python3 manage.py runserver 0.0.0.0:80

CodeDeploy Agent Log location:
/var/log/aws/codedeploy-agent/codedeploy-agent.log







