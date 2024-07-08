from django.shortcuts import render, redirect, Http404

from crud_app2.models import Task


# C z CRUD
def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'crud_app2/task_form.html'
        )
    elif request.method == "POST":
        data = request.POST

        task = data.get('task')
        if task:
            Task.objects.create(name=task)

        return redirect('crud_app2:task_list_view')


# R z CRUD (lista)
def task_list_view(request):

    tasks = Task.objects.all()

    return render(
        request,
        'crud_app2/tasks.html',
        {'tasks': tasks}
    )


# R z CRUD (szczegółu)
def task_detail_view(request, task_id):
    tasks = Task.objects.filter(id=task_id)
    if tasks:
        task = tasks[0]
        task_id = task.id

        return render(
            request,
            'crud_app2/task_detail.html',
            {"task_id": task_id, "task": task}
        )

    else:
        raise Http404()


# U z CRUD
def task_update_view(request, task_id):
    tasks = Task.objects.filter(id=task_id)
    if not tasks:
        raise Http404()
    else:
        task = tasks[0]
        task_id = task.id

    if request.method == "GET":
        return render(
            request,
            'crud_app2/task_update.html',
            {'task_id': task_id, 'task': task}
        )
    elif request.method == "POST":
        data = request.POST

        task_new_name = data.get('task_name')
        if task_new_name:
            task.name = task_new_name
            task.save()

        return redirect('crud_app2:task_list_view')


def task_delete_view(request, task_id):
    tasks = Task.objects.filter(id=task_id)
    if not tasks:
        raise Http404()
    else:
        task = tasks[0]
        task_id = task.id

    if request.method == "GET":
        return render(
            request,
            'crud_app2/task_delete.html',
            {'task_id': task_id, "task": task}
        )

    elif request.method == "POST":
        data = request.POST

        if 'yes' in data:
            task.delete()

        return redirect('crud_app2:task_list_view')
