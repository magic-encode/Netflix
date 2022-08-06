from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from netflixapp.views import CommentAPIView, MovieViewSet, ActorViewSet, CommentDetailAPIView

router = DefaultRouter()
router.register("actor", ActorViewSet, "actor")
router.register("movie", MovieViewSet, "movie")



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
    
    path('commente/<int:comment_pk>/', CommentDetailAPIView.as_view()),
    path('comment/del/', CommentAPIView.as_view(), name="comment"),
]