from django.urls import path

from . import views

urlpatterns = [
    path('', views.LeaveView.as_view(), name='leave'),
]