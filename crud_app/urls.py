from django.urls import path

from crud_app import views

app_name = 'crud_app'


urlpatterns = [
    # C z CRUD
    path('tasks/create/',
         views.task_create_view,
         name='task_create_view'
    ),

    # R z CRUD (lista)
    path('tasks/',
         views.task_list_view,
         name='task_list_view'
    ),

    # R z CRUD (szczegółu)
    path('tasks/<int:task_id>/',
         views.task_detail_view,
         name='task_detail_view'
    ),

    # U z CRUD
    path('tasks/update/<int:task_id>/',
         views.task_update_view,
         name='task_update_view',
    ),

    # D z CRUD
    path('tasks/delete/<int:task_id>/',
         views.task_delete_view,
         name='task_delete_view'
    ),
]
