from django.utils import timezone
from django.db import models as m
import datetime

# Create your models here.
class Question(m.Model):
    question_text = m.CharField(max_length=255)
    pub_date = m.DateTimeField("date Published")

    def __str__(self):
        return self.question_text
    def was_recently_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(m.Model):
    choice_text = m.CharField(max_length=255)
    votes = m.IntegerField(default=0)
    question = m.ForeignKey(Question, on_delete=m.CASCADE)

    def __str__(self):
        return self.choice_text