from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]