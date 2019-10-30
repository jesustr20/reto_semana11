from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    library_code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    pages = models.CharField(max_length=10)
    language = models.CharField(max_length=20)
    copy = models.IntegerField(default=1)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank= True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title   

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    rental_date = models.DateTimeField(
        default=timezone.now)
    return_date = models.DateTimeField(
        blank= True, null=True)

    def __str__(self):
        return f'{self.book} {self.client}'
