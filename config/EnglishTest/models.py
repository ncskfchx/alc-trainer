from django.db import models


class TestModel(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    question = models.CharField(max_length=225)
    true_answer = models.CharField(max_length=225)
    false_answer = models.CharField(max_length=225)
    false_answer2 = models.CharField(max_length=225)
    false_answer3 = models.CharField(max_length=225)

    class Meta:
        db_table = 'question'