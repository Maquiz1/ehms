from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse

def hospital_dashboard(request):
    return render(request, "clinic/hospital_dashboard.html", {})

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("hospital_dashboard"))
    else:
        form = UserCreationForm()
    return render(request, "registration/sign_up.html", {"form": form})


def hospital_admin(request):
    return render(request, "clinic/hospital_admin.html", {})


def medical_dashboard(request):
    return render(request, "clinic/medical_dashboard.html", {})


# def patients_list(request):
#     patients = Patient.objects.all()
#     return render(request, "clinic/patients_list.html", {"patients": patients})


# def add_patients(request):
#     if request.method == "POST":
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("patients_list")  # Redirect to the patients list after adding
#     else:
#         form = PatientForm()
#     return render(request, "clinic/add_patients.html", {"form": form})
