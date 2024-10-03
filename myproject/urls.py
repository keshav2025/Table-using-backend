
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('table', views.home_view, name='home'),
    path('About', views.About_view, name='About'),

    path('admin/', admin.site.urls),
   
    
]
