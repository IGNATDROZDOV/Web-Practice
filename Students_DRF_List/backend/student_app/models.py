from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	patronymic = models.CharField(max_length=100)
	department = models.CharField(max_length=200)


	def __str__(self): 
		return f"{self.name} {self.surname}"