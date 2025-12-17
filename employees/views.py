

# Create your views here.

from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from .models import Department

# Create your views here.

def department_list(request):
    department = Department.objects.all()
    return render(request,"employee/department_list.html",{"department":department})

def employee_list(request):
    employee = Employee.objects.all()
    department = Department.objects.all()
    department_id= request.GET.get('department')
    total_employee = employee.count()
    total_department=department.count()

    if department_id:
        employee = employee.filter(department_id=department_id)
        total_employee = employee.count()
    return render(request,"employee/list.html",{"employee":employee,"department":department,"total_employee":total_employee,"total_department":total_department})

def employee_create(request):
    department=Department.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        department_id =request.POST.get('department')

        Employee.objects.create(name=name, email=email, position=position,department_id=department_id)
        return redirect('employee_list')

    return render(request, 'employee/create.html',{"department":department})

def employee_update(request, id):
    department = Department.objects.all()
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')
        employee.department_id = request.POST.get('department')
        employee.save()
        return redirect('employee_list')

    return render(request, 'employee/update.html', {"employee": employee,"department":department})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')  
