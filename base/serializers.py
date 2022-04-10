from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Topic, Video

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    topic_id = serializers.CharField(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

    def get_videos(self, obj):
        videos = obj.video_set.all()
        serializer = VideoSerializer(videos, many=True)
        return serializer.data