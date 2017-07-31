from django.db import models


# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length=150)
	title = models.CharField(max_length=100, blank=True, null=True)
