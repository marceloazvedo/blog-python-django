from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=256)
    content = models.TextField(max_length=40000)

    def __str__(self):
        return self.title