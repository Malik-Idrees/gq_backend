from rest_framework import serializers
from .models import Course, GoogleLink, Topic, Video, Profile

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    # user = serializers.StringRelatedField(many=False) #user is the foreign key, returns __str__ repr of user model
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username



class VideoSerializer(serializers.ModelSerializer):
    # topic = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='title'
    # )

    topic_id = serializers.CharField(read_only=True)
    topic = serializers.CharField(read_only=True)

    class Meta:
        model = Video
        fields = '__all__' 


class GoogleLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model= GoogleLink
        fields = '__all__' 



class TopicSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField(read_only=True)
    # videos = VideoSerializer(many=True,read_only=True) # Alternative to get_videos Approach, requires related name
    links = GoogleLinkSerializer(many=True,read_only=True) #using related name

    class Meta:
        model = Topic
        fields = '__all__'

    def get_videos(self, obj):
        #obj type : Topic
        # Topic.video_set.all() Retrives all videos associated to topic
        videos = obj.video_set.all() 
        # videos = obj.videos.all() #"videos" as a related name on (FK) in Videos table.
        serializer = VideoSerializer(videos, many=True)
        return serializer.data