from peewee import *

db = SqliteDatabase('my.db')

class user(Model):
    userId = CharField(unique=True)
    class Meta:
        database = db

