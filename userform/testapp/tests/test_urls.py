from django.test import TestCase
from django.urls import reverse,resolve
from testapp import urls
from testapp.views import register,userlogin
from django.test import Client

class Testurls(TestCase):

    def test_resgister(self):
        # self.client.logout()
        data = {"username" :"test","email": "johndoe@admin.com", "password": "password"}
        response = self.client.post('/register/', data)
        self.assertEqual(response.status_code, 404)

    def test_login(self):
        self.client.logout()
        data = {"username" :"test","email": "test@gmail.com", "password": "password"}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 404)

    def test_logout(self):
            self.client = Client()
            self.client.login(username="johndoe@admin.com",
                              password="password")
            response = self.client.get("/logout/")
            self.assertEqual(response.status_code, 302)
