from django.db import models


# Create your models here.
class About(models.Model):
    title = models.charField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
