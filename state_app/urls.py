from django.urls import path

from state_app import views

app_name = 'state_app'


urlpatterns = [
    path('cookies/', views.cookies_view, name='cookies_view'),
    path('form/', views.form_view, name='form_view'),
    path('home/', views.home_view, name='home_view'),

    path('session/', views.session_view, name='session_view'),
]