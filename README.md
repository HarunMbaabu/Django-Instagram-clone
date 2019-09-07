# Lux.com 
# Django File (and Image) Uploads web-page


A photo sharing  web app developed in Django 2.22 and  Bootstrap 4. 

 Requirements:
 
 1)a virtual environment 
      
      Python3 -m venv < env name>
      
 2) Django 2.2.5  and pillow 6.1.0  installed  
 
       pipenv install django==2.2.5 pillow==6.1.0
       
       
  Creating the project.
  
           django-admin startproject insta_project 
           
           
 Creating  the application  for our project
 
 
          python manage.py startapp posts
          
          
Settings.py


                  
          # insta_project/settings.py
          INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'posts.apps.PostsConfig', # new
           ]        
                  
                  
          
         
       
      
      
