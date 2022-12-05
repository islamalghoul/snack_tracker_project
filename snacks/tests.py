from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse


class SnacksTest(TestCase):
    def tests_home_page_status(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Home.html')
