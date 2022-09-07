from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()
    # id_group = models.ForeignKey('Group', on_delete=models.CASCADE)


class Group(models.Model):
    group_name = models.CharField(max_length=30)


class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=80)
    age = models.PositiveIntegerField()
    # student_teacher = models.ManyToManyField()


class Lesson(models.Model):
    lesson_name = models.TextField()


class Article(models.Model):
    article_title = models.CharField(max_length=60, null=False)
    article_text = models.TextField(default="")
    article_writer = models.ForeignKey(Teacher, on_delete=models.CASCADE)
