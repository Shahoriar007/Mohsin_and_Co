from django.shortcuts import render

def home(request):
    return render(request, 'Main_Web_Work/home.html')

def about(request):
    return render(request, 'Main_Web_Work/about.html')

def contacts(request):
    return render(request, 'Main_Web_Work/contacts.html')

def admin_p2(request):
    return render(request, 'Main_Web_Work/admin_p2.html')