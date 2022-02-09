from rest_framework.views import APIView
from .models import Leave, LeaveSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta

class LeaveView(APIView):
    """
    Leave view.
    """

    def date_range(self, start, end):
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        delta = end - start  # as timedelta
        days = [start + timedelta(days=i) for i in range(delta.days + 1)]
        return len(days)

    def get(self, request):
        """
        Return a list of all leave requests.
        """
        pk = request.GET.get('pk')

        if pk:
            leave = Leave.objects.get(pk=pk)
            serializer = LeaveSerializer(leave)
            res = serializer.data
            res['leave_period'] = self.date_range(res['start_date'], res['end_date'])
            return Response(res, status=status.HTTP_200_OK)
        else:
            leaves = Leave.objects.all()
            serializer = LeaveSerializer(leaves, many=True)
            res = serializer.data
            for leave in res:
                leave['leave_period'] = self.date_range(leave['start_date'], leave['end_date'])
            return Response(res, status=status.HTTP_200_OK)
            
    def post(self, request):
        """
        Create a new leave request.
        """
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        Update an existing leave request.
        """
        pk = request.GET.get('pk')

        if pk:
            leave = Leave.objects.get(pk=pk)
            serializer = LeaveSerializer(leave, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Delete an existing leave request.
        """
        pk = request.GET.get('pk')

        if pk:
            leave = Leave.objects.get(pk=pk)
            leave.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

