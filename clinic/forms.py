from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Patient

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        label="Username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        label="Password",
    )

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'age', 'gender', 'unique_id', 'email',
            'mobile_number', 'marital_status', 'occupation', 'blood_group',
            'blood_pressure', 'sugar_level', 'address', 'city', 'state', 'postal_code'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'gender': forms.RadioSelect(),
            'unique_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Unique ID'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'marital_status': forms.Select(attrs={'class': 'form-select'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Occupation'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blood Pressure'}),
            'sugar_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sugar Levels'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Postal Code'}),
        }