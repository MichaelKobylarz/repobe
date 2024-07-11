from django.urls import path

from form_app2 import views


app_name = 'form_app2'

urlpatterns = [
    path(
        'contact1/',
        views.contact_view_1,
        name='contact_view_1'
    ),
    path(
        'contact2/',
        views.contact_view_2,
        name='contact_view_2'
    ),
    path(
        'contact3/',
        views.contact_view_3,
        name='contact_view_3'
    ),
]
