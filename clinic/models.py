from django.contrib.auth.models import AbstractUser, Group, Permission, User  # Import the default User model
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

    def __str__(self):
        return self.username

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

class Staff(models.Model):
    POSITION_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('receptionist', 'Receptionist'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')  # Link to default User model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    specialization = models.CharField(max_length=100, blank=True, null=True)  # Optional for non-doctors
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_position_display()})"
    

class Consultation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, limit_choices_to={'position': 'doctor'})  # Only allow doctors
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',null=True)  # Track consultation status
    created_by = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_consultations')  # Assigned by receptionist

    def __str__(self):
        return f"{self.patient} -> {self.staff} on {self.date} at {self.time} ({self.get_status_display()})"
