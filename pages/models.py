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
        return reverse("pages:post-detail", kwargs={"pk": self.pk})
    #     Here, self is the specific Post object whose method is being called—for example, the post that was just created or edited.
    # If that post’s primary key is 1, then self.pk is 
    # 1. Django passes that value into the URL pattern named "pages:post-detail":
    # The "pk" on the left in kwargs={"pk": self.pk} is the URL parameter name. It must match <int:pk> in the route.
    # The value on the right, self.pk, is the post’s actual database ID. 
    # Django then builds a URL like /post/1/.