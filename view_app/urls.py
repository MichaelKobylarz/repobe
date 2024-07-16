from django.urls import path
from django.views.generic import TemplateView

from view_app import views

app_name = 'view_app'


urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    path('hello3/', views.HelloTemplateView.as_view(), name='hello3'),
    path('hello4/', TemplateView.as_view(template_name='view_app/hello.html'), name='hello4'),

    path('create-person/', views.person_create_view, name='create_person_view'),
    path('create-person2/', views.PersonCreateView.as_view(), name='create_person_view2')
]
