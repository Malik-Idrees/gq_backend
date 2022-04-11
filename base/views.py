from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.data import courses
from base.serializers import CourseSerializer, TopicSerializer, VideoSerializer
from .models import Course, Profile, Topic, Video
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


@api_view(['GET'])
def getCourse(request):
    # return JsonResponse(courses.courses,safe=False)
    user = request.user
    topics = Topic.objects.filter(course=user.course.id)
    
    serializer = TopicSerializer(topics,many=True)
    return Response(serializer.data)


# Get all videos of every topics -> []
@api_view(['GET'])
def getVideos(request):
    user = request.user
    topic = Topic.objects.filter(course=user.course.id)
    data = []
    for topic in topic:
        videos = topic.video_set.all()
        serializer = VideoSerializer(videos, many=True)
        data+=serializer.data
    return Response(data)


@api_view(['GET'])
def test(req):
    video = Video.objects.prefetch_related('topic')
    # video = Video.objects.filter(topic=1).prefetch_related('topic')
    serializer = VideoSerializer(video, many=True)
    print(repr(serializer))
    return Response(serializer.data)