from django.urls import path

from hello import views


urlpatterns = [
    # view intro

    path('', views.hello_view),

    # templates intro
    path('hi/', views.hi_view),
    path('hi2/', views.hi2_view),

    # user input
    path('jurek/', views.jurek_view),
    path('jacek/', views.jacek_view),
    path('ksawier/', views.ksawier_view),
    path('<str:name>/', views.name_view),
    path('<str:name>/2/', views.name_view2)
]