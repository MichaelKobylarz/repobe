from django.urls import path

from hello import views


urlpatterns = [
    # view intro
    path('', views.hello_view),

    # templates intro
    path('hi/', views.hi_view),
    path('hi2/', views.hi2_view),
]