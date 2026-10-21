#!/bin/bash

<< task
Deploy a Django app and handle the code for errors.

task


code_clone() {

    echo "Cloning the django app...."
    git clone https://github.com/LondheShubham153/django-notes-app.git
}

install_requirements() {

    echo "Installing Dependencies..."
    sudo apt-get install docker.io nginx docker-compose -y
}

required_restarts() {

    # sudo systemctl enable docker
    sudo systemctl enable nginx 
    # sudo systemctl restart docker 
}

deploy() {

    docker build -t notes-app .
    # docker run -d -p 8000:8000 notes-app:latest
    docker-compose up -d
}


echo "************* Deployemnt Started *************"

if ! code_clone; then
    echo "the code directory already exists"
    cd django-notes-app
fi

if ! install_requirements; then
    echo "Installation Failed"
    exit 1
fi 

if ! required_restarts; then
    echo "System Fault Identified"
    exit 1
fi

if ! deploy; then
    echo "Deployment Failed, sending mail to admin"
    exit 1
fi

echo "************* Deployemnt Done *************"

