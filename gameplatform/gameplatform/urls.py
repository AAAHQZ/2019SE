"""gameplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from prepare import  prepareViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',prepareViews.index),
    path('logIn/',prepareViews.logIn),
<<<<<<< HEAD
    path('signUp/',prepareViews.signUp),
]
=======
    ]
>>>>>>> a64b58efd2224320ca2e015e23f842682e831093
