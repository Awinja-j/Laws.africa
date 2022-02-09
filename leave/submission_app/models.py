from django.db import models
from rest_framework import serializers

class Leave(models.Model):
    """
    Model representing a leave request.
    """
    leave_requester = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(choices=[('N', 'Normal'), ('S', 'Sick Leave')] )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LeaveSerializer(serializers.Serializer):

    """
    Serialize Leave object
    """
    leave_requester = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    reason = serializers.ChoiceField(choices=[('N', 'Normal'), ('S', 'Sick Leave')])

    class Meta:
        model = Leave
        fields = '__all__'


    def create(self, validated_data):
        """
        Create and return a new `Leave` instance, given the validated data.
        """
        return Leave.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Leave` instance, given the validated data.
        """
        instance.leave_requester = validated_data.get('leave_requester', instance.leave_requester)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
    
    def validate(self, data):
        """
        Validate the data
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date cannot be before start date")

        return data

    