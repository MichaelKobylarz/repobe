from django.shortcuts import render


# Create your views here.
def hello_get(request):
    data = request.GET

    name = None
    if 'name' in data:
        name = data['name']

    return render(
        request,
        'form_app/hello_get.html',
        {'name': name}
    )