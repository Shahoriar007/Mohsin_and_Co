from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="Main_Web_Work-Home"),
    path('about/', views.about, name="Main_Web_Work-about"),
    path('contacts/', views.contacts, name="Main_Web_Work-contacts"),
    path('admin_p2/', views.admin_p2, name="Main_Web_Work-admin_p2"),

]