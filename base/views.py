from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from base.data import courses
# Create your views here.
def getRoutes(request):
    routes= [
        '/api/course/', #Get all courses(Only one)
        '/api/course/create/', #Post
        '/api/course/<id>/',
        '/api/course/<id>/topic/', #Get
        '/api/course/<id>/topic/create/', #Post
        '/api/topic/<id>/video/', #Get
        '/api/topic/<id>/video/create', #Post
    ]
    return JsonResponse(routes,safe=False)

def getCourse(request):
    # return HttpResponse(courses.courses, content_type="application/json")
    return JsonResponse(courses.courses,safe=False)