from django.test import TestCase
from .models import *

# Create your tests here.
class APIUserMethodTests(TestCase):

    # Set up an instance of the APIUser class
    def setUp(self):

        self.model_instance = APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

    def test_get_username(self):

        username = self.model_instance.get_username()
        correct_username = "dalye54"
        self.assertEqual(username, correct_username)
    
    def test_get_firstName(self):

        first_name = self.model_instance.get_firstName()
        correct_first_name = "Eoin"
        self.assertEqual(first_name, correct_first_name)

    def test_get_lastName(self):

        last_name = self.model_instance.get_lastName()
        correct_last_name = "Daly"
        self.assertEqual(last_name, correct_last_name)

    def test_get_email(self):

        email = self.model_instance.get_email()
        correct_email = "eoin.daly54@mail.dcu.ie"
        self.assertEqual(email, correct_email)

    def test_get_full_name(self):
        full_name = self.model_instance.get_full_name()
        correct_full_name = "Eoin Daly"
        self.assertEqual(full_name, correct_full_name)

    def test_print_user_details(self):
        print_format = str(self.model_instance)
        correct_print_format = f'Username: dalye54\nFirst Name: Eoin\nLast Name: Daly\nEmail: eoin.daly54@mail.dcu.ie'
        self.assertEqual(print_format, correct_print_format)