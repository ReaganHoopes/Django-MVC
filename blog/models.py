from datetime import datetime

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    posted = models.DateTimeField('date posted')

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    commenter = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    posted = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.commenter