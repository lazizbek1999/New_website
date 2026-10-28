from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    
    def __str__(self):
     return self.title
    
    def get_absolute_url(self):
        return reverse("pages:post_detail", kwargs={"pk": self.pk})
    #        ^^       ^^^^^^^
#        |        the post's actual number (e.g. 2), from the model
#        the NAME of the URL capture, from <int:pk> in urls.py