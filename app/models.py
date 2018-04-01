from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

class Book(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=50)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'

class Subject(models.Model):
    content = models.CharField(max_length=512, null=True)
    type = models.IntegerField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    img_url = models.ImageField(upload_to='books/%Y/%m/%d/')

