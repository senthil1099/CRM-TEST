from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Employee
from .serializers import EmployeeSerializer

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('contacts:list'))
        else:
            messages.error(request,'username or password not correct')
            return redirect(reverse('login'))
        
                
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def signoff(request):
    logout(request)
    return redirect("employees:login")


@login_required
def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeSerializer(request.POST)
        if employee_form.is_valid():
            employee = employee_form.save(commit=False)
            employee.user = request.user
            employee.save()
            return redirect('employee_list')

    else:
        employee_form = EmployeeSerializer()

    return render(request, 'employee_form.html', {'employee_form': employee_form})


@login_required
def employee_list(request):
    employees = Employee.objects.filter(user=request.user)
    return render(request, 'employee_list.html', {'employees': employees})

