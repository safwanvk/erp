from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendence/', views.view_attendence, name='view-attendence')
]
