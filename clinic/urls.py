from django.urls import path, include
from clinic import views
from .views import CustomLoginView, SignUpView
from .views import add_patient,patients_list,delete_patient,patient_dashboard

urlpatterns = [
    path("", views.hospital_dashboard, name="hospital-dashboard"),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('add-patient/', add_patient, name='add-patient'),
    path('patients-list/', patients_list, name='patients-list'),
    path('edit-patient/<int:patient_id>/', add_patient, name='edit-patient'),  # For editing an existing patient
    # Other URL patterns...
    path("delete-patient/", delete_patient, name="delete-patient"),
    # Other URL patterns...
    # path("delete-patient/", delete_patient, name="delete-patient"), Ijavascript used no need to pass id
    path("patient-dashboard/<int:patient_id>/", patient_dashboard, name="patient-dashboard"),
]
