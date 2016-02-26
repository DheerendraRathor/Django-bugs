from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    pass


class Video(models.Model):
    pass


class Concept(models.Model):
    group = models.ForeignKey(Group, related_name='concepts')

    videos = models.ManyToManyField(Video, related_name='concepts')


class Marker(models.Model):
    video = models.ForeignKey(Video, related_name='markers')


class Quiz(models.Model):
    pass


class QuizHistory(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quiz_histories')
    user = models.ForeignKey(User, related_name='quiz_histories')


class QuizMarker(Marker):
    quiz = models.ForeignKey(Quiz)
