<h2> <center> Lux.Com </center> </h2> 
<b> Django Files and feeds Uploads web-page </b>


A photo sharing  web app developed in Django 2.22 and  Bootstrap 4. 

 Requirements:
 
 1)A virtual environment 
      
      Python3 -m venv < env name>
      
 2) Django 2.2.5  and pillow 6.1.0  installed  
 
       pipenv install django==2.2.5 pillow==6.1.0
       
       
  Creating the project.
  
           django-admin startproject < project name  > 
           
           
 Creating  the application  for our project
 
 
          python manage.py startapp posts
          
          
# Settings.py


                  
          # insta_project/settings.py
          INSTALLED_APPS =
          [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'posts.apps.PostsConfig', # new
           ]        
                 
    
          
                 
Now run python manage.py migrate to setup the new database for our project.                 
                  
  
             
  # Models              
             from django.db import models
             class Post(models.Model):
                title = models.TextField()
                cover = models.ImageField(upload_to='images/')

                def __str__(self):
                  return self.title
                  
                  
                  
# MEDIA_ROOT                  
              # insta_project/settings.py
              MEDIA_URL = '/media/'
              MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
              
              
              
              (insta) $ mkdir media
              (insta) $ mkdir media/images
              
              
              
#Admin


              # posts/admin.py
              from django.contrib import admin

              from .models import Post

              admin.site.register(Post)
              
              
         
  Then run the folloeing  commands           

 
           python manage.py makemigrations
           python manage.py migrate
           
           
           
           
 creating a superuser account to access the admin and then execute runserver to spin up the local web server for the first time.


           (insta) $ python manage.py createsuperuser
           (insta) $ python manage.py runserver
           
           
           
      


Displaying posts which means urls.py, views.py, and template files.

#  Preview


![alt text](https://djangocentral.com/wp-content/uploads/2019/03/ezgif.com-video-to-gif.gif)




