from django.shortcuts import render, redirect
# from .models import Patient
# from .forms import PatientForm

def home(request):
    return render(request, "clinic/home.html", {})


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
