from .models import Staff

def staff_context(request):
    if request.user.is_authenticated:
        staff = Staff.objects.filter(user=request.user).first()
        return {'staff': staff}
    return {}