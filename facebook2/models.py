from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Story(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	tag = models.CharField(max_length=100)