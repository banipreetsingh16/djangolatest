from django.db import models

# Create your models here.

# class Blog(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=150)
#     description = models.TextField()
#     is_published = models.BooleanField(default=False)
#     #published_on = models.DateTimeField(auto_now=True)

class DataBase(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_experience = models.CharField(max_length=50)
    latest_education_degree = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)

    