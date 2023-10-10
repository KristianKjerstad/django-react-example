from django.urls import path, re_path

from students.views import StudentsView, StudentView

# base "api/students"
urlpatterns = [
    path("", StudentsView.as_view()),
    # path("", views.add_student, name="add_student"),
    re_path(r"([0-9])$", StudentView.as_view()),
]
