from django.test import TestCase, Client
from django.urls import reverse

from .views import index_view, sign_up_view
from .models import CustomUser

class Views_Test_Cases(TestCase):

    def test_index_view(self):
        # Make a GET request to the view using reverse to get the URL
        response = self.client.get(reverse("index"))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the template 'website/index.html' was used
        self.assertTemplateUsed(response, "website/index.html")

class Sign_Up_View_Test_Case(TestCase):

    # Test setUp
    def setUp(self):
        CustomUser.objects.create(username="test_user", password="test_password")
        self.client = Client()

    # Check if status code is 200
    def test_sign_up_status_code(self): 
        response = self.client.get(reverse("sign_up"))
        self.assertEqual(response.status_code, 200)
        
    # Check if template "sign_up.html" was used
    def test_sign_up_template_used(self): 
        response = self.client.get(reverse("sign_up"))
        self.assertTemplateUsed(response,"website/sign_up.html")

    # Check if passwords do not match
    def test_sign_up_password_match(self): 
        response = self.client.post(reverse('sign_up'), {
            'username': 'test_user',
            'password_1': 'password123',
            'password_2': 'password456',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords do not match")
    
    # Check if username exists in database
    def test_sign_up_username_exists(self):
        response = self.client.post(reverse("sign_up"), {
            "username": "test_user",
            "password_1": "test_password",
            "password_2": "test_password",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username already exists")
        self.assertTrue(CustomUser.objects.filter(username="test_user").exists())

    # def test_sign_up_redirect_to_log_in(self):
    #     response = self.client.post(reverse('sign_up'), {
    #         'username': 'test_user',
    #         'password_1': 'test_password',
    #         'password_2': 'test_password',
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response.url, reverse("log_in"))