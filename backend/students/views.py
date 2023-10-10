import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import status

from students.serializers import StudentSerializer

from .models import Student


@method_decorator(csrf_exempt, name="dispatch")
class StudentsView(TemplateView):
    template_name = "students"

    def get(self, request):
        """Get all students"""
        data = Student.objects.all()
        serializer = StudentSerializer(data, context={"request": request}, many=True)
        return HttpResponse(json.dumps(serializer.data), status=status.HTTP_200_OK, content_type="application/json")

    def post(self, request):
        """Add a single student"""
        print(json.loads(request.body))
        serializer = StudentSerializer(data=json.loads(request.body))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(TemplateView):
    template_name = "student"

    def get(self, request, student_id):
        """Get a single student"""
        data = get_object_or_404(Student, pk=student_id)
        serializer = StudentSerializer(data, context={"request": request}, many=False)
        return HttpResponse(json.dumps(serializer.data), status=status.HTTP_200_OK, content_type="application/json")
