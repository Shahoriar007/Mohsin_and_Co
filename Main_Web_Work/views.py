from django.shortcuts import render

def home(request):
    return render(request, 'Main_Web_Work/home.html')

def about(request):
    return render(request, 'Main_Web_Work/about.html')
