from django.db import models

class TestModel(models.Model):
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()