from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name = 'student'

def index(request):
    return render(request, 'student/index.html')

def view_attendence(request):
    return render(request, 'student/attendence.html')

def attendence_details(request):
    return render(request, 'student/attendence_details.html')

def view_marks(request):
    return render(request, 'student/marks.html')

def view_timetable(request):
    return render(request, 'student/timetable.html')