from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  

    path('form/', views.form),  
    path('edit/<int:person_id>/', views.edit),  
    path('delete/<int:person_id>/', views.delete),  
]