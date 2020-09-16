from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="Main_Web_Work-Home"),
    path('about/', views.about, name="Main_Web_Work-about"),

]