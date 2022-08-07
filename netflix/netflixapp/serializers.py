from rest_framework import serializers

from .models import Movie,  Comment, Actor



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'birthdate', 'gender']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'year', 'genre', 'actors']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'movie', 'user', 'text', 'created_date']

    



