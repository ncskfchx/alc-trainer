from django.db import models


class TestModel(models.Model):
    question = models.CharField(max_length=225)
    true_answer = models.CharField(max_length=225)
    false_answer = models.CharField(max_length=225)
    false_answer2 = models.CharField(max_length=225)
    false_answer3 = models.CharField(max_length=225)

    class Meta:
        db_table = 'question'



class ProgressModel(models.Model):
    username = models.CharField(max_length=225, unique=True)
    progress = models.IntegerField()
    count_question = models.IntegerField()
    true_count_question = models.IntegerField()
    false_count_question = models.IntegerField()

    class Meta:
        db_table = 'progress'