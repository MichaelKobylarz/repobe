from django.shortcuts import render, redirect, Http404

TASKS = [
    'kodowanie',
    'zmywanie'
]


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
            TASKS.append(task)

        return redirect('crud_app2:task_list_view')


# R z CRUD (lista)
def task_list_view(request):

    tasks = TASKS

    return render(
        request,
        'crud_app2/tasks.html',
        {'tasks': tasks}
    )


# R z CRUD (szczegółu)
def task_detail_view(request, task_id):
    if 0 < task_id <= len(TASKS):
        task = TASKS[task_id-1]

        return render(
            request,
            'crud_app2/task_detail.html',
            {"task_id": task_id, "task": task}
        )

    else:
        raise Http404()


# U z CRUD
def task_update_view(request, task_id):
    if not 0 < task_id <= len(TASKS):
        raise Http404()
    else:
        task = TASKS[task_id-1]

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
            TASKS[task_id-1] = task_new_name

        return redirect('crud_app2:task_list_view')


def task_delete_view(request, task_id):
    if not 0 < task_id <= len(TASKS):
        raise Http404()
    else:
        task = TASKS[task_id-1]

    if request.method == "GET":
        return render(
            request,
            'crud_app2/task_delete.html',
            {'task_id': task_id, "task": task}
        )

    elif request.method == "POST":
        data = request.POST

        if 'yes' in data:
            TASKS.pop(task_id-1)

        return redirect('crud_app2:task_list_view')
