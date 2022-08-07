from django.db import models



class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthdate = models.DateTimeField(blank=False)
    gender = models.BooleanField(null=True)


    def __str__(self) -> str:
        return self.name