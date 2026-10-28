from django.test import TestCase
from pages.models import Post
from django.contrib.auth import get_user_model
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.post = ... stores that object=text> (str words) on the class under the name post.
        # Every test can now reach it as self.post
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        # Creates a Post row. author=cls.user links the post to the user you just made. 
        # It’s saved as cls.post, so tests use it as self.post. 
        # In a fresh test database, this first post gets pk=1
        cls.post = Post.objects.create(
            title='A good title',
            body="This is a test!",
            author=cls.user,
            )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.body, 'This is a test!')
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
        
        