from rest_framework import serializers
from .models import students


class studentsSerializer(serializers.Serializer):
    class Meta:
        model = students
        fields = ('id',
                  'first',
                  'last',
                  'email_id',
                  'phone')
