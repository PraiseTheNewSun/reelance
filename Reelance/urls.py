"""
URL configuration for Reelance project.

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
from django.urls import path
from lance import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout', views.LogOut, name='logout'),

    # TALENT URLS
    path('talent/dashboard/', views.TalentDashboard, name='talent-dashboard'),
    path('talent/applications/', views.TalentApplications, name='applications'),
    path('talent/jobs/', views.TalentJobs, name='jobs'),
    path('talent/profile/', views.TalentProfile, name='profile'),
    path('talent/hires/', views.TalentHires, name='hires'),

    # CLIENT URLS
    path('client/dashboard/', views.ClientDashboard, name='client-dashboard'),
    path('client/profile', views.ClientProfile, name='client-profile'),
    path('client/jobs', views.ClientJobs, name='client-jobs'),
    path('client/applications', views.ClientApplications, name='client-applications'),
    path('client/hires', views.ClientHires, name='client-hires'),
    path('client/profile-update', views.ClientProfileUpdate, name='update-client')
]
