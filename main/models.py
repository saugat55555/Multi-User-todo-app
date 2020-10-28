from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MainModel(models.Model):
	task = models.CharField(max_length=300)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.task