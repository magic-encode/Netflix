from django.contrib import admin

from .models import Actor
from .models import Comment
from .models import Movie


admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Comment)
