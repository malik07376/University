from django.db import models

class Faculty(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()

class Professor(models.Model):
    user=models.CharField(max_length=30)
    department=models.ForeignKey("Faculty", on_delete=models.PROTECT, null=True)
    title=models.CharField(max_length=25)
    bio=models.TextField()

class Student(models.Model):
    user=models.CharField(max_length=30)
    department=models.ForeignKey("Faculty", on_delete=models.PROTECT, null=True)
    enrollment_date=models.DateTimeField()
    graduation_date=models.DateTimeField()

class Course(models.Model):
    name=models.CharField(max_length=30)
    code=models.IntegerField()
    description=models.TextField()
    department = models.ForeignKey("Faculty", on_delete=models.PROTECT, null=True)
    professor = models.ForeignKey("Professor", on_delete=models.PROTECT, null=True)

class Cabinet(models.Model):
    room_number=models.IntegerField()
    building=models.CharField(max_length=30)
    capasity=models.IntegerField()
