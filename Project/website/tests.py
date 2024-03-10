from django.test import TestCase
from django.urls import reverse

from .views import index_view

class Views_Test_Cases(TestCase):

    def test_index_view(self):
        # Make a GET request to the view using reverse to get the URL
        response = self.client.get(reverse("index"))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the template 'website/index.html' was used
        self.assertTemplateUsed(response, "website/index.html")