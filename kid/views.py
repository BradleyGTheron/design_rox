from django.shortcuts import render
from print.models import Print

def kid(request):
    kid_prints = Print.objects.filter(enable = True, category = 1, home_page = False)
    return render(request, 'kid/kid.html', {'kid_prints': kid_prints})

# Create your views here.
