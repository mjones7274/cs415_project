# cs415_project
Project for CS415 semester

Creating a website using virtual machines as the backend for a semester project


#!/bin/bash
sudo apt update -y
sudo apt install ruby wget -y
cd /home/ubuntu
sudo wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto
sudo apt install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2

