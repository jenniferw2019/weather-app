# Weather App using Django

## Introduction
Build a Django App that displays the current weather for various cities. The current weather data is provided by Open Weather Map API

## Prerequisites
This project will require Python installed

## Step 1 - Setting Up the Project
Installing Django:

- $ pipenv install django
- $ pipenv install requests
- $ pipenv shell

## Step 2 - Starting a Django Project
Once you have Django installed, run the startproject command to generate the project

- $ django-admin startproject weather

Navigate to the new directory and use manage.py to run the sunserver command

- $ python manage.py runserver

By default, the URL for the app should be 127.0.0.1:8000

## Step 3 - Logging into the Admin Dashboard
Stop the server with CTRL+C, and then run the migrate command

- $ python manage.py migrate

By running this command, Django has created a SQLite database which is the default database in the settings.

To create an admin user, run the createsuperuser command, follow the instructions by providing a username, email address, and password for your admin user.

- $ python manage.py createsuperuser

Once finished, start the server again and visit the admin dashboard by going to 127.0.0.1:8000/admin

## Step 4 - Creating the App

Stop the server, then run the startapp command

- $ python manage.py startapp weather

## Step 4 - Adding the Template and View

A template in Django is an HTML file that allows for extra syntax that makes the template dynamic. In your case, crate a new file called index.html, which will be your main template.

Views in Django are either functions or classes. Now that you have your template created, let's create a view and URL combination so you can actually see this in your app.

## Step 6 - Using the Weather API

Using Open Weather Map API to get real time weather for any cities that you add to your app.

## Step 7 - Displaying the Data in the Template

Create a table in the database to hold the cities that you want to show the weather for.

## Step 8 - Creating the Form

Create a form so that the user can add a city directly via the form.



