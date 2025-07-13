from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class PassportAPITest(APITestCase):
    def test_api_root(self):
        """Test the API root endpoint"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertIn('endpoints', response.data)

    def test_passport_extract_endpoint(self):
        """Test the passport extract endpoint"""
        url = reverse('passport-extract')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertIn('status', response.data)
