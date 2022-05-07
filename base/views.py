from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.data import courses
from base.serializers import CourseSerializer, ProfileSerializer, TopicSerializer, VideoSerializer
from .models import Course, Profile, Topic, Video

from django.contrib.auth import get_user_model
User = get_user_model()
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

#Tested for errors
@api_view(['GET','POST'])
def getCourse(request):
    # return JsonResponse(courses.courses,safe=False)
    user = request.user

    try:
        topics = Topic.objects.filter(course=user.course.id)
    except Course.DoesNotExist:
        return Response({"error":"Content does not exist.Generate?"})
    
    serializer = TopicSerializer(topics,many=True)
    return Response(serializer.data)


# Get all videos of every topics -> []
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getVideos(request):
    user = request.user
    topicList = Topic.objects.filter(course=user.course.id)
    data = []
    for topic in topicList:
        videos = topic.video_set.all()
        serializer = VideoSerializer(videos, many=True)
        data+=serializer.data
    return Response(data)


#Tested for errors
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user

    if request.method == 'POST':
        data = request.data
        profile = Profile.objects.filter(user=user).exists()
        if(profile): 
            return Response({'error':'profile already exists'}, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.create(
            user=user,
            expertiseLevel=data['expertiseLevel'],
            goalToAchieve=data['goalToAchieve'],
            profession=data['profession'],
            dailyTime=data['dailyTime']
        )
        serializer = ProfileSerializer(profile,many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    if request.method == 'GET':
        # from django.shortcuts import get_object_or_404
        # profile = get_object_or_404(Profile, user=user)
        # serializer = ProfileSerializer(profile,many=False)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile,many=False)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error':'profile does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        

    
@api_view(['GET'])
def test(req):
    video = Video.objects.prefetch_related('topic')
    # video = Video.objects.filter(topic=1).prefetch_related('topic')
    serializer = VideoSerializer(video, many=True)
    print(repr(serializer))
    return Response(serializer.data)