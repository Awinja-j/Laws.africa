from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Leave

class LeaveModelTestCase(TestCase):
    '''
    Test module for Leave model

    '''
    def setUp(self):
        self.leave = Leave.objects.create(
            leave_requester='John Doe',
            start_date='2020-01-01',
            end_date='2020-01-01',
            reason='I need a vacation',
            status='P'
        )

    def test_leave_model_can_create_a_leave(self):
        self.assertIsInstance(self.leave, Leave)

    def test_leave_model_can_create_a_leave_with_a_requester(self):
        self.assertEqual(self.leave.leave_requester, 'John Doe')

    def test_edit_leave_request(self):
        self.leave.leave_requester = 'Jane Doe'
        self.leave.save()
        self.assertEqual(self.leave.leave_requester, 'Jane Doe')

    def test_delete_leave_request(self):
        self.leave.delete()
        self.assertEqual(self.leave.leave_requester, '')

class LeaveRequestAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        self.client = APIClient()
        self.leave_request = {
            'leave_requester': 'John Doe',
            'start_date': '2020-01-01',
            'end_date': '2020-01-01',
            'reason': 'I need a vacation',
            'status': 'P'
        }
        self.client.post(self.leave_request, format=json)

    def test_api_can_create_a_leave_request(self):
        """Test the api has leave creation capability."""
        response = self.client.post('/leave/', self.leave_request, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_list_all_leave_requests(self):
        """Test the api can list all leave requests."""
        response = self.client.get('/leave/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_leave_request(self):
        """Test the api can get a given leave."""
        leave = Leave.objects.get()
        response = self.client.get(f'/leave/{leave.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, leave)

    def test_api_can_update_leave_request(self):
        leave = Leave.objects.get()
        change_leave = {'leave_requester': 'Jane Doe'}
        res = self.client.put(f'/leave/{leave.id}/', change_leave, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_leave_request(self):
        leave = Leave.objects.get()
        response = self.client.delete(f'/leave/{leave.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



