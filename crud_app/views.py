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
            'crud_app/task_form.html'
        )
    elif request.method == "POST":
        data = request.POST

        task = data.get('task')
        if task:
            TASKS.append(task)

        return redirect('crud_app:task_list_view')


# R z CRUD (lista)
def task_list_view(request):

    tasks = TASKS

    return render(
        request,
        'crud_app/tasks.html',
        {'tasks': tasks}
    )


# R z CRUD (szczegółu)
def task_detail_view(request, task_id):
    if 0 < task_id <= len(TASKS):
        task = TASKS[task_id-1]

        return render(
            request,
            'crud_app/task_detail.html',
            {"task_id": task_id, "task": task}
        )

    else:
        raise Http404()
