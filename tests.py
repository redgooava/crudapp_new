from django.contrib.auth.models import User
from django.test import TestCase


class ViewsTestCase(TestCase):

    def test_no_questions(self):
        response = self.client.get('/crudapp/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/crudapp/login/')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get('/crudapp/create')
        self.assertEqual(response.status_code, 200)


class test_login(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test',
            'password': 'Serjeri12051988'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/crudapp/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
