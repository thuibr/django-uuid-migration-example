import uuid
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    id = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    author_old = models.IntegerField()

