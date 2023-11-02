from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
