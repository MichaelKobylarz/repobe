from django.urls import path

from form_app import views

app_name = 'form_app'


urlpatterns = [
    path('hello-get/', views.hello_get, name='hello_get'),
]
