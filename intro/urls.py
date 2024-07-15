"""
URL configuration for intro project.

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
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('link/', include('link_app.urls')),
    path('form/', include('form_app.urls')),
    path('crud/', include('crud_app.urls')),
    path('orm/', include('orm_app.urls')),
    path('crud2/', include('crud_app2.urls')),
    path('form2/', include('form_app2.urls')),
    path('state/', include('state_app.urls')),
]