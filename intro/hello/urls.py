from django.urls import path

from hello.views import hello_view


urlpatterns = [
    path('main/', hello_view),
]