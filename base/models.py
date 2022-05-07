from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.

class Course(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.category)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    expertiseLevel = models.CharField(max_length=200, null=True, blank=True) #Beginner || Intermediate || Expert
    goalToAchieve = models.CharField(max_length=200, null=True, blank=True) #Software engineer
    profession = models.CharField(max_length=200, null=True, blank=True) #Android Development
    dailyTime = models.IntegerField(null=True, blank=True,default=0)
    

    def __str__(self):
        return str(self.user)

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class Video(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    views = models.IntegerField(null=True, blank=True, default=0)
    href = models.CharField(max_length=500,null=True, blank=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)