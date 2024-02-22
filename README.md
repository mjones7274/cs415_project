# cs415_project
Project for CS415 semester

Creating a website using virtual machines as the backend for a semester project

EC2 Initialization Script

nginx
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
sudo mkdir -pv /var/log/gunicorn/
sudo mkdir -pv /var/run/gunicorn/
sudo chown -cR ubuntu:ubuntu /var/log/gunicorn/
sudo chown -cR ubuntu:ubuntu /var/run/gunicorn/
sudo apt-get install nginx -y
sudo systemctl start nginx



apache
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
sudo apt install apache2 -y
sudo apt install libapache2-mod-wsgi-py3 -y
sudo systemctl start apache2
sudo systemctl enable apache2

sudo apt install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2

sudo chmod 755 /home/ubuntu
sudo chmod -R a+rwx env


Ubuntu:
Change mysqlclient to 2.1.1 in requirements.txt
push to repo
CodeDeploy to Instance
cd /home/ubuntu/cs415_api
sudo python3 -m venv env
sudo chmod 755 /home/ubuntu
sudo chmod -R a+rwx env
source env/bin/activate
pip install -r requirements.txt
sudo vim /etc/apache2/sites-available/000-default.conf
sudo systemctl restart apache2



000-default.conf:
        <Directory /home/ubuntu/cs415_api/cs415>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess cs415 python-home=/home/ubuntu/cs415_api/env python-path=/home/ubuntu/cs415_api
        WSGIProcessGroup cs415
        WSGIScriptAlias / /home/ubuntu/cs415_api/cs415/wsgi.py


Mysql Client
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install mysqlclient

start server
sudo python3 manage.py runserver 0.0.0.0:80

CodeDeploy Agent Log location:
/var/log/aws/codedeploy-agent/codedeploy-agent.log

sudo service codedeploy-agent status


