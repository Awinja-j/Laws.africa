from django.test import TestCase

class LeaveRequestTestCase(TestCase):
    def test_list_leave_requests(self):
        response = self.client.get('/leave/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave/leave_list.html')

    def test_submit_leave_request(self):
        response = self.client.get('/leave/submit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave/leave_submit.html')

    def test_edit_exsiting_leave_request(self):
        response = self.client.get('/leave/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave/leave_edit.html')


