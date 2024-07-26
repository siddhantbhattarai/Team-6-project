"""
URL configuration for kavyalaya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

handler404 = 'portfolio.views.custom_404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("django.contrib.auth.urls")),
    path('user/', include('user.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', include('portfolio.urls')),
    path('', include('postapp.urls')),
    path('dash', include('dash.urls')),
#    path("upload/", custom_upload_function, name="upload"),
    
]