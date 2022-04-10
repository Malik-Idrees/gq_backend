from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name='routes'),
    path('course/',views.getCourse,name='course'),
    path('videos/',views.getVideos,name='videos'),
    path('test/',views.test,name='videos') #Just For Experiments
]