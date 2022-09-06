from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()


class Group(models.Model):
    group_name = models.CharField(max_length=30)


class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()


class Lesson(models.Model):
    lesson_name = models.TextField()
