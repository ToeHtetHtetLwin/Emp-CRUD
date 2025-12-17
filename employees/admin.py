from django.contrib import admin
from .models import Employee
from .models import Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)