#from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.TextField()
    description = models.CharField(max_length= 200, blank=True)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title