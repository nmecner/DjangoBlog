from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    content = models.TextField()    