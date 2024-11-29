from django.db import models
from django.contrib.auth.models import User

class EmployeeImage(models.Model):
    EmployeeID = models.CharField(max_length=100, unique=True)
    Image = models.ImageField(upload_to='employee_images/')

def create_user(username, email, password):
    user = User.objects.create_user(username, email, password)
    return user

