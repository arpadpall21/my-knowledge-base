from django.db import models


class User(models.Model):
    user = models.TextField(primary_key=True)


class Post(models.Model):
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
