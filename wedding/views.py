from django.shortcuts import render

def wedding(request):
    return render(request, 'wedding/wedding.html')
