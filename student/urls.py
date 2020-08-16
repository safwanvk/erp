from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('attendence/', views.view_attendence, name='view-attendence'),
    path('attendence-details', views.attendence_details, name='attendence-details'),
    path('marks/', views.view_marks, name='view-marks')
]
