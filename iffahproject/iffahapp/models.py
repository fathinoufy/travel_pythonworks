from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __self__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=280)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __self__(self):
        return self.name






