# cs415_project
Installation for Django API

## EC2 Install Commands
## Ubuntu
- Allow Inbound Rules
  - SSH
  - HTTP
  - HTTPS
- Attach IAM Role to Instance
- User Data
```
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
```
## SSH into the Instance
- Validate CodeDeploy Agent is installed and running:
  `sudo service codedeploy-agent status`
- Validate Apache is installed and running:
  `sudo systemctl status apache2`

## Deploy Notes
- Deploy Project files into
  `/home/ubuntu/cs415_api/`
- Create a virtual Environment for python dependencies, cd into `/home/ubuntu/cs415_api/` run the following commands:
```
sudo python3 -m venv env
sudo chmod 755 /home/ubuntu
sudo chmod -R a+rwx env
source env/bin/activate
pip install -r requirements.txt
```

## Apache Setup
- You will need to edit the 000-default.conf file located in `/etc/apache2/sites-available/`
```
sudo vim /etc/apache2/sites-available/000-default.conf
```
- Keep all the current text in the file and add the following code inside the end of the `<VirtualHost>` tag:
```
        <Directory /home/ubuntu/cs415_api/cs415>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess cs415 python-home=/home/ubuntu/cs415_api/env python-path=/home/ubuntu/cs415_api
        WSGIProcessGroup cs415
        WSGIScriptAlias / /home/ubuntu/cs415_api/cs415/wsgi.py
```
- Save the file and restart apache
```
sudo systemctl restart apache2
```


Ugly Admin
python manage.py collectstatic




