from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'), 
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('testimonials/', views.testimonials, name='testimonial'),
    path('appointment/', views.appointment, name='appointment'),
    path('features/', views.features, name='features'),
    path('team/', views.team, name='team'),
    path('404/',views.error_404, name='404'),
]