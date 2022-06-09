from asyncio.windows_events import NULL
import imp
from django.db import models
from django.forms import CharField
import jsonfield


class student(models.Model):
    studid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    details = jsonfield.JSONField()
    class Meta:
        db_table = 'employeetable'


class course(models.Model):
     course_id = models.OneToOneField(student,on_delete=models.CASCADE,primary_key=True)
     course_name = models.CharField(max_length=30)

class result(models.Model):
    result_id=models.OneToOneField(course,on_delete=models.CASCADE,primary_key=True)
    result_grade = models.FloatField()
# Create your models here.
