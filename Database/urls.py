"""
URL configuration for Database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from curacao_devices_db.views import DepartmentsView, DevicesView, LocationsView, SignupView,  TransactionsView, VueView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),

    #path('', VueView, name='index'),
    
    path('departments/', DepartmentsView.as_view()),
    path('devices/', DevicesView.as_view()),
    path('locations/', LocationsView.as_view()),
    path('signup/', SignupView.as_view()),
    path('transactions/', TransactionsView.as_view())
]
