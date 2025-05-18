from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=''), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('staff/', views.staff, name='staff'),
    
    path('staff/', views.staff, name='staff_list'),
    path('staff/add/', views.staff_add, name='staff_add'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('s/<int:pk>/delete/', views.staff_delete, name='staff_delete'),

    path('diseases/', views.diseases, name='disease_type'),
    path('d/add/', views.disease_add, name='disease_add'),
    path('d/<int:pk>/', views.disease_detail, name='disease_detail'),
    path('d/<int:pk>/edit/', views.disease_edit, name='disease_edit'),
    path('d/<int:pk>/delete/', views.disease_delete, name='disease_delete'),
     
    path('patients/', views.patients, name='patients'),
    path('p/add/', views.patient_add, name='patient_add'),
    path('p/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('p/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('p/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
]

