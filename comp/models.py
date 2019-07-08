from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    year = models.DateField()
    count = models.IntegerField()
    class Meta:
        db_table = "books"