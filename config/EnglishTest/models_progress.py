from peewee import *


conn = SqliteDatabase('/Users/macbookpro/Documents/EnglishTest/config/db.sqlite3')

class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше


class ProgressModel(BaseModel):
    username = CharField(max_length=225, unique=True)
    progress = IntegerField()
    count_question = IntegerField()
    true_count_question = IntegerField()
    false_count_question = IntegerField()

    class Meta:
        table_name = 'progress'