from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.serializers import CourseSerializer, ProfileSerializer, TopicSerializer, VideoSerializer
from .models import Course, Profile, Topic, Video

from django.contrib.auth import get_user_model
User = get_user_model()

# Test Data
from base.data import courses
from base.data import topics

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

@api_view(['GET', 'POST'])
def getCourse(request):
        user = request.user

        if request.method == 'GET':

            try:
                topics_list = Course.objects.filter(user=user)
            except:
                return Response({"message":"No courses foun"})
            
            serializer = CourseSerializer(topics_list,many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            data = request.data
            goalToAchieve = data['goalToAchieve']

            course = Course.objects.create(
                user=user,
                goalToAchieve=data['goalToAchieve'],
                expertiseLevel=data['expertiseLevel'],
                jobRequired=data['jobRequired'],
                dailyTime=data['dailyTime'],
            )

            # Processing and supposed topics output
            for topic in topics.topics:

                #Only Add a skill if it has relevant videos
                if len(topic['data']):
                    newSkill = Topic.objects.create(
                        course=course,
                        title=goalToAchieve,
                    )

                    for data in topic['data']:
                        if len(data):
                            print(data)
                        video = Video.objects.create(
                            topic=newSkill,
                            title=data['title'],
                            # views=data['views'].split()[0][:-1], #Store a number instead of str like `212k views` 
                            views=data['views'], 
                            href=data['href'],
                        )
                        print("video added to topic")

            return Response({'message':'Success'}, status=status.HTTP_201_CREATED)
            # serializer = CourseSerializer(course,many=False)



@api_view(['GET'])
def getCourseDetail(request, pk):
    # return JsonResponse(courses.courses,safe=False)
    user = request.user

    if request.method == 'GET':

        try:
            topics_list = Topic.objects.filter(course=pk)
        except Course.DoesNotExist:
            return Response({"error":"Content does not exist.Generate?"})
        
        serializer = TopicSerializer(topics_list,many=True)
        return Response(serializer.data)



# Get all videos of every topic -> []
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getVideos(request):
    user = request.user

    courses = Course.objects.filter(user=user)
    data = []

    for course in courses:

        topicList = Topic.objects.filter(course=course)
        # print(topicList[0].course)
        serializer = TopicSerializer(topicList, many=True)

        data+=serializer.data

    response = [( Response({'message':'no videos'}, status=status.HTTP_200_OK)), Response(data)] [len(data)>0]
    return response



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