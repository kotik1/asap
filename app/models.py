from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	email = models.CharField(max_length=100, blank=True)
	

class Task(models.Model):
	created_by = models.ForeignKey(UserProfile)
	done_by = models.ForeignKey(UserProfile, related_name="done_by_r", blank=True,  null=True)
	done =  models.BooleanField(default=False)
	created_date = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=5000)
