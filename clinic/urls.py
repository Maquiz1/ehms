from django.urls import path, include
from clinic import views
from .views import CustomLoginView, SignUpView
from .views import add_patient,patients_list,delete_patient,patient_dashboard,assign_consultation,consultations_list,delete_consultation,doctor_dashboard, add_consultation, update_consultation

urlpatterns = [
    path("", views.hospital_dashboard, name="hospital-dashboard"),
    path("medical-dashboard/", views.medical_dashboard, name="medical-dashboard"),
    path("dentist-dashboard/", views.dentist_dashboard, name="dentist-dashboard"),
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
    
    path('assign-consultation/', assign_consultation, name='assign-consultation'),
    path('consultation-list/', consultations_list, name='consultation-list'),
    path('edit-consultation/<int:consultation_id>/', assign_consultation, name='edit-consultation'),  # For editing an existing consultation
    # path("delete-consultation/", delete_consultation, name="delete-consultation"),
    # path("consultation-dashboard/<int:consultation_id>/", consultation_dashboard, name="consultation-dashboard"),
    path('doctor-dashboard/', doctor_dashboard, name='doctor-dashboard'),
    
    path('consultations/', consultations_list, name='consultations-list'),
    path('consultations/add/', add_consultation, name='add-consultation'),
    path('consultations/update/<int:consultation_id>/', update_consultation, name='update-consultation'),
    path('consultations/delete/<int:consultation_id>/', delete_consultation, name='delete-consultation'),
]
