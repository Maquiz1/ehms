from django.contrib import admin
from .models import Staff, Patient, Consultation

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'specialization', 'email', 'phone_number')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'mobile_number')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'staff', 'date', 'time', 'notes')
    list_filter = ('date',)
    search_fields = ('patient__first_name', 'patient__last_name', 'staff__first_name', 'staff__last_name')