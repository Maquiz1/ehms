from django.urls import path, include
from clinic import views
from .views import CustomLoginView, SignUpView
from .views import add_patient,patients_list

urlpatterns = [
    path("", views.hospital_dashboard, name="hospital_dashboard"),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('add-patient/', add_patient, name='add-patient'),
    path('patients-list/', patients_list, name='patients-list'),
]
