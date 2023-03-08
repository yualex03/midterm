from django.urls import path
from students.views import student_list, student_create, student_detail

urlpatterns = [
    path('api/student/', student_list, name='student-list'),
    path('api/students/', student_create, name='student-create'),
    path('api/students/<int:id>/', student_detail,name='student-detail')
]
