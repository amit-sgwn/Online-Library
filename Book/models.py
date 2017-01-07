from django.db import models

import datetime
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_isbn = models.CharField(max_length=25)
    page = models.IntegerField(default=0)
    no_of_copies = models.IntegerField(default=0)
    book_subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=50)
    tag = models.TextField()
    
    def __str__(self):
        return self.book_name
    
    def num_of_copies(self):
        return self.no_of_coies
    
    def sub(self):
        return self.book_subject
    
class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.sub_name
    
