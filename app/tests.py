from django.test import TestCase
from django.core.urlresolvers import resolve
from app.views import home, new_client
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_loads(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_html(self):
        print("Testing to make sure that the home screen looks right")
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('app/index.html')
        self.assertEqual(response.content.decode(), expected_html)

from app.models import Client
class ClientModelTest(TestCase):

	def test_add_new_client(self):
		client = Client(first_name='John', last_name='Doe', email_address='john@example.org')
		client.save()
		test_client = Client.objects.first()
		self.assertEqual(test_client.first_name, 'John')