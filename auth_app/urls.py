from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.home, name='home'),
    path(
        'login/',
        views.login_view,
        name='login_view'
    ),
    path(
        'logout/',
        views.logout_view,
        name='logout_view'
    )
]
