from django.http import Http404
from .models import Actor
from .models import Movie
from .models import Comment

from .serializers import ActorSerializer
from .serializers import MovieSerializer
from .serializers import CommentSerializer

from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer

    queryset = Actor.objects.all()


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  
    search_fields = ['name']
    filterset_fields = ['genre']  
    
    @action(detail=True, methods=["POST"], url_path='add-actor')
    def add_actor(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["actor_id"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actors.add(actor)
        movie.save()
        return Response({'status': 'success'})
    
    @action(detail=True, methods=["DELETE"], url_path='remove-actor')
    def remove_actor(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["actor_id"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actors.remove(actor)
        movie.save()
        return Response({'status': 'success'})
        
    @action(detail=True, methods=['GET'])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actor.all(), many=True)

        return Response(serializer.data)


class CommentDetailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get_object(self, comment_pk):
        try:
            return Comment.objects.get(id=comment_pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, comment_pk):

        comment = self.get_object(comment_pk)
        comment_serializer = CommentSerializer(comment)
        comment = comment_serializer.data

        return Response(data=comment)

    def delete(self, request, comment_pk, format=None):
        snippet = self.get_object(comment_pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()

    
    
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(data=serializer.data)


    def post(self, request):
        request.data['user']=request.user.id
        serializer = CommentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    # def perform_create(self, serializer):
    #     serializer.validated_data['user'] = self.request.user
    #     serializer.save()


# def get(self, request, format=None):
    #     usernames = [user.username for user in User.objects.all()]
    #     return Response(usernames)
