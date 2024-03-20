from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from .models import CustomUser

class Index_View_Test_Cases(TestCase):

    # Test setup
    def setUp(self):
        self.client = Client()

    # Check that the response status code is 200
    def test_index_view_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    # Check that the template 'website/index.html' was used
    def test_index_view_template_used(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "website/index.html")

class Sign_Up_View_Test_Case(TestCase):

    # Test setup
    def setUp(self):
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
        CustomUser.objects.create(username="test_user", password="test_password")
        response = self.client.post(reverse("sign_up"), {
            "username": "test_user",
            "password_1": "test_password",
            "password_2": "test_password",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username already exists")
        self.assertTrue(CustomUser.objects.filter(username="test_user").exists())

    # Check for redirection to log_in page after registration
    def test_sign_up_redirect_to_log_in(self):
        response = self.client.post(reverse('sign_up'), {
            'username': 'test_user',
            'password_1': 'test_password',
            'password_2': 'test_password',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("log_in"))

class Log_in_View_Test_Case(TestCase):

    # Test setup
    def setUp(self):
        self.client = Client()

    # Check if status code is 200
    def test_log_in_status_code(self): 
        response = self.client.get(reverse("log_in"))
        self.assertEqual(response.status_code, 200)

    # Check if template "log_in.html" was used  
    def test_log_in_template_used(self): 
        response = self.client.get(reverse("log_in"))
        self.assertTemplateUsed(response,"website/log_in.html")

    # Check for invalid credentials
    def test_log_in_for_invalid_credentials(self):
        CustomUser.objects.create(username="test_user", password="test_password")
        response = self.client.post(reverse('log_in'), {
            'username': 'test_user',
            'password': 'test_password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid log in credentials")
        
    # Check for user authentication
    def test_log_in_user_authentication(self):
        CustomUser.objects.create(username="test_user", password=make_password("test_password"))
        login_successfull = self.client.login(username="test_user", password="test_password")
        self.assertTrue(login_successfull)

    # Check for redirection to home page
    def test_log_in_redirection_to_home(self):
        CustomUser.objects.create(username="test_user", password=make_password("test_password"))
        response = self.client.post(reverse('log_in'), {
            'username': 'test_user',
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home")) 