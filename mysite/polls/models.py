import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='avatars/', verbose_name='Аватар')

    def __str__(self):
        return self.username

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.TextField(max_length=500, verbose_name='Описание вопроса')
    image = models.ImageField(upload_to='questions_images/', verbose_name='Изображение')
    question_votes = models.IntegerField(verbose_name="Количество проголосовавших", default=0)
    pub_date = models.DateTimeField('date published')

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(seconds=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def percentage(self):
        percents = self.votes * 100 / self.question.question_votes
        return percents

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)