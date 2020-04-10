from django.shortcuts import render

def party(request):
    return render(request, 'party/party.html')

# Create your views here.
