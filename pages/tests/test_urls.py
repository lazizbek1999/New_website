from django.test import TestCase
from pages.models import Post
from django.urls import reverse

class PostModelTests(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('pages:home'))
        self.assertTemplateUsed(response, 'pages/post_list.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Message Board Homepage')