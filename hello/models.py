from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=128)

# Create your models here.
class Author(models.Model):

    imie = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=128)
    rok = models.IntegerField()
    #book_set -> prez related name w ksiażkach to zamienia sie na napisane_ksiazki
    #wydane_ksiazki
    #address

class Address(models.Model):
    street = models.CharField(max_length=123)
    city = models.CharField(max_length=123)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

class Publisher(models.Model):
    name = models.CharField(max_length=123)
class Book(models.Model):
    title = models.CharField(max_length=123)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,
                               related_name='napisane_ksiazki')
    publisher = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,
                                  related_name='wydane_ksiazki')
    genres = models.ManyToManyField(Genre)
    publisher = models.ManyToManyField(Publisher)