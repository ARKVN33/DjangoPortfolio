from django.db import models


# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=100)
    percent = models.IntegerField()

    def __str__(self):
        return self.title
