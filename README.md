# Pinit-App

## By Christine Mwangi

## Table of contents

+ [Description](#Description)
+ [Installation process](#installation-process)
+ [Technologies used](#technologies-used)
+ [Known-Bugs](#known-bugs)
+ [Contact Information](#contact-information)
+ [Copyright and License](#copyright-and-license-information)

## Description

Pinit-App is an application that allows users to upload photos,create accounts  and comment on other people's posts.

Application Features include:

1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

The following is a live link to the project:

## Installation process

To access my repository link:
[Click here](https://github.com/nyakiochristine/pinit-app.git)

*To clone this repository locally, type the following command on your terminal.*

If using HTTP keys, type:

`https://github.com/nyakiochristine/pinit-app.git`

If using SSH keys, then type:

`git@github.com:nyakiochristine/pinit-app.git`

On running the commands successfully, you should have a local version of this repository.
Navigate to the target directory and open it with a prefered IDE :

1. On running the application, type the following on the terminal;

+ `python3 manage.py runserver`

 To test the application;

+ `python3 manage.py test;

 To navigate to a local browser, Type this on a preferred browser:

### Create a Virtual Environment

Run the following commands in the same terminal:
`sudo apt-get install python3.8-venv`
`python3.8 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies

Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Create a database

psql

CREATE DATABASE instagram;

### .env file

SECRET_KEY = '<Secret_key>'
DBNAME = 'instagram'
USER = '<Username'
PASSWORD ='password'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email>'
EMAIL_HOST_PASSWORD = 'your-password>'

## Run initial Migration

python3.8 manage.py makemigrations instaapp
python3.8 manage.py migrate

### Running the app in development

In the same terminal type:
`python3 manage.py runserver`

Open the browser on `http://localhost:8000/`

+ `127.0.0.1:5000`

## Technologies used

+ [Python3.8](https://www.python.org/)

+ [Django](https://www.djangoproject.com/)
+ [Heroku](https://heroku.com)

## Known-Bugs

Application runs smoothly. No bugs identified.

## Contact information

Feel free to contact me:

+ Author E-mail ; `chrissymwangi254@gmail.com`

## Copyright and License

[MIT LICENSE](https://github.com/nyakiochristine/BlogA/community/license/new?branch=main&template=mit)
