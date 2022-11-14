from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'gender', 'birthday',
            'address', 'phone_number', 'aff_school', 'class_level', 'created_at')
