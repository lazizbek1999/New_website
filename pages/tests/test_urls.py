from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from pages.models import Post


class PostViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="A good title",
            body="This is a test!",
            author=cls.user,
        )

    def test_homepage(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "Django blog")

    def test_detail_view(self):
        response = self.client.get(
            reverse("pages:post-detail", kwargs={"pk": self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/post_detail.html")
        self.assertContains(response, "A good title")
        self.assertContains(response, "This is a test!")

    def test_detail_view_404(self):
        wrong_response = self.client.get(
            reverse("pages:post-detail", kwargs={"pk": 999})
        )
        self.assertEqual(wrong_response.status_code, 404)

    def test_login(self):
        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': 'secret',
                'email': 'test@email.com',
            },
        )
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        
        
    def test_protected_page_redirects_to_login(self):
        response = self.client.get(reverse("pages:post-new"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response.url)