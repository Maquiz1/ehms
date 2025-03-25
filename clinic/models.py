from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Avoid conflict with the default User model
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Avoid conflict with the default User model
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    unique_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    sugar_level = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.unique_id})"
