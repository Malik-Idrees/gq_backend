from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.

class Course(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goalToAchieve = models.CharField(max_length=200, null=True, blank=True)
    expertiseLevel = models.CharField(max_length=200, null=True, blank=True)
    jobRequired = models.BooleanField(default=False)
    dailyTime = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.goalToAchieve)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True) #John
    age = models.IntegerField(null=True, blank=True,default=0)
    profession = models.CharField(max_length=200, null=True, blank=True) #Android Developer
    expertiseLevel = models.CharField(max_length=200, null=True, blank=True) #Beginner || Intermediate || Expert
    

    def __str__(self):
        return str(self.user)

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    note = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class GoogleLink(models.Model):
    topic = models.ForeignKey(Topic,related_name='links' ,on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class Video(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    views = models.CharField(max_length=200, null=True, blank=True)
    href = models.CharField(max_length=500,null=True, blank=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)