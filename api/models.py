from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserManager(models.Manager):
    def unatural_key(self):
    	return self.username
    User.natural_key=unatural_key

class Notepad(models.Model):
    title=models.CharField(max_length=500)
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    editing=models.BooleanField(default=False)

    objects=UserManager()

    def __str__(self):
        return self.title

    class meta:
        unique_together=(('username','title'),)
        index_together=(('username','title'),)

    def natural_key(self):
    	return (self.username)

class Image(models.Model):
	image=models.ImageField()
	username=models.ForeignKey(User, on_delete=models.CASCADE)
	show=models.BooleanField(default=False)

	def __str__(self):
		return self.image

	class meta:
		unique_together=(('username','image'),)