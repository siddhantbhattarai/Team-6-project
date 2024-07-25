from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationViews.as_view(), name="register"),
    path('login/', views.UserLoginViews.as_view(), name="login"),
    path('logout/', views.UserLogoutViews.as_view(), name="logout"),
]
