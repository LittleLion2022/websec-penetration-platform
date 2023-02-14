"""websec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from login import views as login_views
from portscan import views as portscan_views
from dirscan import views as dirscan_views
from vulscan import views as vulscan_views
from vulsearch import views as vulsearch_views
from dnssearch import views as dnssearch_views
from api import views as api_views
urlpatterns = [
	path('',login_views.login),
	path('admin/', admin.site.urls),
	path('index/',login_views.index),
    path('register/',login_views.register),
    path('logout/',login_views.logout),
    path('change-password/',login_views.change_password),
    path('api-management/',api_views.show),
    path('port-scan/',portscan_views.scanner),
    path('dir-scan/',dirscan_views.scanner),
    path('dns-search/',dnssearch_views.scanner),
    path('vul-scan/',vulscan_views.scanner),
    path('vul-search/',vulsearch_views.scanner),
]
