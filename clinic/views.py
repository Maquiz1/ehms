from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm, PatientForm, ConsultationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Patient
from django.contrib import messages
from .models import Patient, Consultation
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Consultation, Staff
from datetime import datetime
from django.utils.timezone import now
from django.utils.timezone import make_aware


def hospital_dashboard(request):
    patients = Patient.objects.all()
    patient_count = Patient.objects.count()  # Count all patients
    # patient_count = patients.count()  # Get the count of patients
    context = {      
        "patients": patients,
        "patient_count": patient_count
    }
    return render(request, "clinic/hospital-dashboard.html", context)

# /clinic/views.py
class SignUpView(FormView):
    template_name = "registration/sign_up.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("hospital-dashboard")

    def form_valid(self, form):
        user = form.save()  # Save the user
        login(self.request, user)  # Log the user in
        return super().form_valid(form)

def hospital_admin(request):
    return render(request, "clinic/hospital_admin.html", {})


# def medical_dashboard(request):
#     return render(request, "clinic/medical-dashboard.html", {})

def dentist_dashboard(request):
    return render(request, "clinic/dentist-dashboard.html", {})


def patients_list(request):
    patients = Patient.objects.all()
    patient_count = patients.count()  # Get the count of patients
    return render(request, "patients/patients-list.html", {"patients": patients, "patient_count": patient_count})

# def add_patients(request):
#     if request.method == "POST":
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("patients_list")  # Redirect to the patients list after adding
#     else:
#         form = PatientForm()
#     return render(request, "clinic/add_patients.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = CustomLoginForm

def add_patient(request, patient_id=None):
    if patient_id:
        # If patient_id is provided, fetch the existing patient for editing
        patient = get_object_or_404(Patient, id=patient_id)
    else:
        # Otherwise, create a new patient instance
        patient = None

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients-list')  # Redirect to the patients list page
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/add-patient.html', {'form': form, 'patient': patient})


def patient_dashboard(request, patient_id=None):
    if patient_id:
        # Retrieve the specific patient's details
        patient = get_object_or_404(Patient, id=patient_id)
        return render(request, "patients/patient-dashboard.html", {"patient": patient})
    else:
        # Handle the case where no patient_id is provided
        messages.error(request, "No patient selected.")
        return redirect("patients-list")  # Redirect to the patients list page

def delete_patient(request):
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
            messages.success(request, "Patient deleted successfully.")
        except Patient.DoesNotExist:
            messages.error(request, "Patient not found.")
    return redirect("patients-list")

@login_required
def assign_consultation(request):
    if not request.user.groups.filter(name='Receptionist').exists():
        raise PermissionDenied("You do not have permission to assign consultations.")
    
    receptionist = get_object_or_404(Staff, user=request.user)  # Get the logged-in receptionist

    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.created_by = receptionist  # Assign the receptionist
            consultation.save()
            return redirect('consultations-list')  # Redirect to the consultations list
    else:
        form = ConsultationForm()
    return render(request, 'consultations/assign-consultation.html', {'form': form})

@login_required
def medical_dashboard(request):
     # Get the logged-in user's staff profile
    staff = Staff.objects.filter(user=request.user, position='doctor').first()
    if not staff:
        # messages.error(request, "You do not have access to the medical dashboard.")
        # return redirect('hospital-dashboard') 
        print(f"403 Error: User {request.user.username} is not a doctor.")
        return render(request, '403.html', status=403)  # Show a 403 error if the user is not a doctor

    # Get consultations assigned to this doctor
    consultations = Consultation.objects.filter(staff=staff).order_by('date', 'time')
    patient_count = consultations.count()  # Get the count of patients
    
    # Determine the greeting based on the current time
    # current_hour = datetime.now().hour
    current_hour = now().hour

    # print(current_hour)
    # print(f"Current hour: {current_hour}, Full datetime: {now()}")
    naive_datetime = datetime.now()  # Naive datetime
    aware_datetime = make_aware(naive_datetime)  # Convert to timezone-aware datetime
    current_hour = aware_datetime.hour

    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"
        
    context = {      
        "consultations": consultations,
        "patient_count": patient_count,
        "staff": staff,  # Pass the staff instance to the template
        "greeting": greeting,  # Pass the greeting to the template
    }

    return render(request, 'clinic/medical-dashboard.html', context)

@login_required
def consultations_list(request):
    # Get the logged-in doctor's consultations
    staff = Staff.objects.filter(user=request.user, position='doctor').first()
    if not staff:
        return render(request, '403.html', status=403)

    consultations = Consultation.objects.filter(staff=staff).order_by('date', 'time')
    return render(request, 'clinic/consultations-list.html', {'consultations': consultations})

def consultation_dashboard(request):
    consultations = Consultation.objects.all()
    return render(request, 'clinic/consultations-list.html', {'consultations': consultations})

def consultation_dashboar(request):
    consultations = Consultation.objects.all()
    return render(request, 'clinic/consultations-list.html', {'consultations': consultations})


def delete_consultation(request):
    consultations = Consultation.objects.all()
    return render(request, 'clinic/consultations-list.html', {'consultations': consultations})

@login_required
def doctor_dashboard(request):
    # Get the logged-in user's staff profile
    staff = Staff.objects.filter(user=request.user, position='doctor').first()
    if not staff:
        print(f"403 Error: User {request.user.username} is not a doctor.")
        return render(request, '403.html', status=403)  # Show a 403 error if the user is not a doctor

    # Get consultations assigned to this doctor
    consultations = Consultation.objects.filter(staff=staff).order_by('date', 'time')

    return render(request, 'clinic/doctor-dashboard.html', {'consultations': consultations})

@login_required
def add_consultation(request):
    staff = Staff.objects.filter(user=request.user, position='doctor').first()
    if not staff:
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.staff = staff  # Assign the logged-in doctor
            consultation.save()
            return redirect('consultations-list')
    else:
        form = ConsultationForm()

    return render(request, 'clinic/add-consultation.html', {'form': form})

@login_required
def update_consultation(request, consultation_id):
    staff = Staff.objects.filter(user=request.user, position='doctor').first()
    if not staff:
        return render(request, '403.html', status=403)

    consultation = get_object_or_404(Consultation, id=consultation_id, staff=staff)

    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultations-list')
    else:
        form = ConsultationForm(instance=consultation)

    return render(request, 'clinic/update-consultation.html', {'form': form})

@login_required
def delete_consultation(request, consultation_id):
    staff = Staff.objects.filter(user=request.user, position='doctor').first()
    if not staff:
        return render(request, '403.html', status=403)

    consultation = get_object_or_404(Consultation, id=consultation_id, staff=staff)
    if request.method == 'POST':
        consultation.delete()
        return redirect('consultations-list')

    return render(request, 'clinic/delete-consultation.html', {'consultation': consultation})