from django.db import models
from .movie import Movie
from django.contrib.auth import get_user_model


User = get_user_model()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Commented by {}'.format(self.user)
    