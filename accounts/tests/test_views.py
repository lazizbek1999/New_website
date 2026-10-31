from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    def test_signup_page_loads(self):
        response = self.client.get(reverse("accounts:signup"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_valid_signup_creates_user_and_redirects(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {"username": "testuser", 
             "password1": "Warsaw2026@", 
             "password2": "Warsaw2026@"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:login"))
        self.assertTrue(get_user_model().objects.filter(username="testuser").exists())
