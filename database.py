from peewee import *
from os import path

database_path = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(database_path, "MyDatabase.db"))
