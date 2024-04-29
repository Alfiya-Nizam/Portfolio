from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    
    skills = models.TextField()
    education = models.CharField(max_length=100)
    work_experience = models.TextField()
    certifications = models.TextField()
    accomplishments = models.TextField()
    
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    image=models.ImageField(upload_to='pictures')
  


    def __str__(self):
        return '{}' .format(self.name)
    

class ProjectDetails(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '{}' .format(self.name)


class ExperienceDetails(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sdate = models.DateField()
    edate = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return '{}' .format(self.name)
    
class EducationDetails(models.Model):
    name = models.CharField(max_length=100)
    sdate = models.DateField()
    edate = models.DateField()
    university = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)

    def __str__(self):
        return '{}' .format(self.name)    


    
    






    
    