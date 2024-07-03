from django.shortcuts import render


# Create your views here.
def hello_get(request):
    data = request.GET

    name = None
    if 'first_name' in data:
        name = data['first_name']

    return render(
        request,
        'form_app/hello_get.html',
        {'name': name}
    )


def show(request):
    data = request.GET

    name = None
    if 'first_name' in data:
        name = data['first_name']

    return render(
        request,
        'form_app/show.html',
        {'name': name}
    )


def hello_post(request):
    data = request.POST
    name = data.get('first_name')

    return render(
        request,
        'form_app/hello_post.html',
        {'name': name}
    )
