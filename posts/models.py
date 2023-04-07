from django.db import models

"""
class Post:
    title: str
    author: str
    content: str
    thumbnail: image
"""

class Post(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=45)
    content=models.TextField()
    thumbnail=models.ImageField(upload_to='media/', default='default.png')
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Post: {self.title}>"

