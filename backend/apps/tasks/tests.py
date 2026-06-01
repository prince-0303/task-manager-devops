from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class TaskAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_unauthenticated_access_denied(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_task(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/tasks/', {
            'title': 'Test Task',
            'priority': 'high'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_only_see_own_tasks(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        self.client.force_authenticate(user=other_user)
        self.client.post('/api/tasks/', {'title': 'Other task'})

        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(len(response.data), 0)
