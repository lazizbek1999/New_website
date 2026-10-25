from django.test import TestCase, SimpleTestCase

class HomepageTests(SimpleTestCase):   
    def test_url_exists_at_correct_location(self):
     response = self.client.get("/")
     self.assertEqual(response.status_code, 201)
     
class AboutpageTests(SimpleTestCase):
 def test_url_exists_at_correct_location(self):
    response = self.client.get('/about')
    self.assertEqual(response.status_code, 200)