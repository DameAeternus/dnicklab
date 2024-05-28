from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    typeColor = [
        ("h", "hard"), ("s", "soft")
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover = models.CharField(choices=typeColor, max_length=2)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    image = models.ImageField()
# Create your models here.
