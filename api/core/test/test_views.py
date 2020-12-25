from django.test import TestCase, Client
from django.urls import reverse


class RegisterTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.register = reverse('register')

    def test_register_POST(self):
        response = self.c.post(self.register, {'email': 'jondoe@gmail.com', 'password': 'Qwerty12345', 'first_name': 'jon', 'last_name': 'doe', 'phone_number': '1234567890', 'pincode': '123456'})
        print(response)
        self.assertEquals(response.status_code, 201)


class LoginTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.register = reverse('register')
        self.login = reverse('login')

    def test_login_POST(self):
        response_register = self.c.post(self.register,
                                        {'email': 'jondoe@gmail.com', 'password': 'Qwerty12345', 'first_name': 'jon',
                                         'last_name': 'doe', 'phone_number': '1234567890', 'pincode': '123456'})
        response_login = self.c.post(self.login, {'email': 'jondoe@gmail.com', 'password': 'Qwerty12345'})
        self.assertEquals(response_register.status_code, 201)
        self.assertEquals(response_login.status_code, 200)

    def test_login_fail_POST(self):
        response_register = self.c.post(self.register,
                                        {'email': 'jondoe@gmail.com', 'password': 'Qwerty12345', 'first_name': 'jon',
                                         'last_name': 'doe', 'phone_number': '1234567890', 'pincode': '123456'})
        response_login = self.c.post(self.login, {'email': 'jondoe@gmail.com', 'password': 'Tfscrad123'})
        self.assertEquals(response_register.status_code, 201)
        self.assertEquals(response_login.status_code, 400)
