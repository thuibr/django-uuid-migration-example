import uuid
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

