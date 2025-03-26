from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm, PatientForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Patient
from django.contrib import messages


def hospital_dashboard(request):
    return render(request, "clinic/hospital_dashboard.html", {})

# /clinic/views.py
class SignUpView(FormView):
    template_name = "registration/sign_up.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("hospital_dashboard")

    def form_valid(self, form):
        user = form.save()  # Save the user
        login(self.request, user)  # Log the user in
        return super().form_valid(form)

def hospital_admin(request):
    return render(request, "clinic/hospital_admin.html", {})


def medical_dashboard(request):
    return render(request, "clinic/medical_dashboard.html", {})


def patients_list(request):
    patients = Patient.objects.all()
    return render(request, "patients/patients-list.html", {"patients": patients})


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