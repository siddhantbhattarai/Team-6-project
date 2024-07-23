from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('careers', views.careers, name='careers'),
    path('contact', views.contact, name='contact'),
    path('privacy-policy', views.about, name='privacy-policy'),
    path('terms-of-service', views.termsofservice, name='termsofservice'),
    path('teams', views.about, name='teams'),
]
