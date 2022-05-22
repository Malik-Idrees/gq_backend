from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name='routes'),
    path('course/',views.courseHandler,name='course'),
    path('course/<int:pk>',views.getCourseDetail,name='course'),
    path('profile/',views.profile,name='profile'),
    path('videos/',views.getVideos,name='videos'),
    path('test/',views.test,name='test') #Just For Experiments
]