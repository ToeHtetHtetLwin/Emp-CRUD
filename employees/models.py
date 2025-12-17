from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

