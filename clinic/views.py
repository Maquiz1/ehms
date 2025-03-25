from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

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


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = CustomLoginForm
