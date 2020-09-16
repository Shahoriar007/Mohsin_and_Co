from django.contrib import admin
from django.urls import path, include

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('Main_Web_Work.urls')),

]
