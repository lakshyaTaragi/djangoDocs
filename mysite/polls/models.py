import datetime

from django.db import models
# Create your models here.\
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200) #required argument --> databse schema and validation
    pub_date = models.DateTimeField('date published') #human readable name of field
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) #relationship between fields
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text