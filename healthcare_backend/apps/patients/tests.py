from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.patients.models import Patient

User = get_user_model()

class PatientTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(email='testuser@example.com', password='password')
        self.client.login(email='testuser@example.com', password='password')

    def test_create_patient(self):
        url = '/api/patients/'
        data = {
            'name': 'John Doe',
            'age': '19',
            'gender': 'Male',
            'condition': 'Flu',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().name, 'John Doe')

    def test_get_patients(self):
        url = '/api/patients/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_patient_permissions(self):
        another_user = User.objects.create_user(email='anotheruser@example.com', password='password')
        self.client.login(email='anotheruser@example.com', password='password')
        url = '/api/patients/'
        data = {
            'name': 'John Doe',
            'age': '19',
            'gender': 'Male',
            'condition': 'Flu',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
        self.client.login(email='testuser@example.com', password='password')
        url = f'/api/patients/{response.data["id"]}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)