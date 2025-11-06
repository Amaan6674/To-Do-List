from django.db import models
from django.contrib.auth.models import User
class TaskModel(models.Model):
	us=models.ForeignKey(User,on_delete=models.CASCADE)
	task=models.CharField(max_length=200)
	task_dt=models.DateTimeField(auto_now_add=True)
	is_completed=models.BooleanField(default=False)
# Create your models here.
