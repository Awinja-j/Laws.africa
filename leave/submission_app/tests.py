from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
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
            reason='S',
        )
        self.assertEqual(Leave.objects.count(), 1)

    def test_leave_model_can_create_a_leave(self):
        self.assertIsInstance(self.leave, Leave)

    def test_edit_leave_request(self):
        self.leave.leave_requester = 'Jane Doe'
        self.leave.save()
        self.assertEqual(self.leave.leave_requester, 'Jane Doe')

    def test_delete_leave_request(self):
        self.leave.delete()
        self.assertEqual(Leave.objects.count(), 0)

class LeaveRequestAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        self.client = APIClient()
        self.leave_request = {
            'leave_requester': 'John Doe',
            'start_date': '2020-01-01',
            'end_date': '2020-01-05',
            'reason': 'N',
            'status': 'P'
        }
        self.client.post('/leave/', self.leave_request, format='json')
        self.assertEqual(Leave.objects.count(), 1)
        self.leave = Leave.objects.get()


    def test_api_can_create_a_leave_request(self):
        """Test the api has leave creation capability."""
        leave_request = {
            'leave_requester': 'Joan Doe',
            'start_date': '2020-01-01',
            'end_date': '2020-01-06',
            'reason': 'S',
            'status': 'P'
        }
        response = self.client.post('/leave/', leave_request, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_list_all_leave_requests(self):
        """Test the api can list all leave requests."""
        response = self.client.get('/leave/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_leave_request(self):
        """Test the api can get a given leave."""
        self.assertEqual(self.leave.leave_requester, 'John Doe')
        response = self.client.get(f'/leave/?pk={self.leave.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['leave_requester'], 'John Doe')

    def test_api_can_update_leave_request(self):
        change_leave = {
            "leave_requester": "honey Doe",
            "start_date": "2020-01-01",
            "end_date": "2020-01-05",
            "reason": "S",
            "status": "P"
              } 
        res = self.client.put(f'/leave/?pk={self.leave.id}', change_leave, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_leave_request(self):
        # leave = Leave.objects.get()
        response = self.client.delete(f'/leave/?pk={self.leave.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



