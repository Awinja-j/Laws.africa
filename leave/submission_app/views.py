from django.http.response import HttpResponse
from django.views.generic import View
from .models import Leave, LeaveSerializer

class LeaveView(View):
    """
    Leave view.
    """
    def get(self, request, pk=None):
        """
        Return a list of all leave requests.
        """
        if pk is None:
            leaves = Leave.objects.all()
            serializer = LeaveSerializer(leaves, many=True)
            return HttpResponse(serializer.data)
        else:
            leave = Leave.objects.get(pk=pk)
            serializer = LeaveSerializer(leave)
            return HttpResponse(serializer.data)

    def post(self, request):
        """
        Create a new leave request.
        """
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

    def update(self, request, pk):
        """
        Update an existing leave request.
        """
        leave = Leave.objects.get(pk=pk)
        serializer = LeaveSerializer(leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
        return HttpResponse(status=400)

    def delete(self, request, pk):
        """
        Delete an existing leave request.
        """
        leave = Leave.objects.get(pk=pk)
        leave.delete()
        return HttpResponse(status=204)
    

