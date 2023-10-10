from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # TODO Student.keys + pk
        fields = ("pk", "name", "email", "document", "phone", "registrationDate")
