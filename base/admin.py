from django.contrib import admin
from .models import Course, Profile, Topic, Video
# Register your models here.

admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Video)