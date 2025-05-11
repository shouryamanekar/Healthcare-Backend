from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from apps.doctors.models import Doctor
from apps.accounts.models import User


class DoctorTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='password')
        self.client.login(email='testuser@example.com', password='password')

    def test_create_doctor(self):
        url = '/api/doctors/'
        data = {
            'name': 'Dr. Smith',
            'specialty': 'Cardiology',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 1)
        self.assertEqual(Doctor.objects.get().name, 'Dr. Smith')

    def test_get_doctors(self):
        url = '/api/doctors/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)