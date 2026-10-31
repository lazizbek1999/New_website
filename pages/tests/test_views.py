from django.test import TestCase
from pages.models import Post
from django.urls import reverse


def test_post_createview(self):
    response = self.client.post(
        reverse("pages:post-new"),
        {
            "title": "New title",
            "body": "New text",
            "author": self.user.id,
        },
    )
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Post.objects.last().title, "New title")
    self.assertEqual(Post.objects.last().body, "New text")

def test_post_updateview(self): # new
    response = self.client.post(
        reverse("pages:post-edit", args="1"),
        {
        "title": "Updated title",
        "body": "Updated text",
        },
    )
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Post.objects.last().title, "Updated title")
    self.assertEqual(Post.objects.last().body, "Updated text")
    
def test_post_deleteview(self): # new
    response = self.client.post(reverse("pages:post-delete", args="1"))
    self.assertEqual(response.status_code, 302)