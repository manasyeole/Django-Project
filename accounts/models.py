from django.db import models


# Create your models here.
class City(models.Model):
	name  = models.CharField(max_length=25)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'cities'


class CSRD(models.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=50)

	def __str__(self):
		return self.username
