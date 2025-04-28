from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('login', views.signin, name='login'),
    path("logout", views.signoff, name="logout"),
    path('employee/create/', views.create_employee, name='create_employee'),
    path('employee/list/', views.employee_list, name='employee_list'),
]

