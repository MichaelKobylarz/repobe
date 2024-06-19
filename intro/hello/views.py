from django.shortcuts import render, HttpResponse


# Create your views here.
def hello_view(request):
    return HttpResponse("Witaj świecie!")


def hi_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <h2>Hello, world!</h2>
        </body>
    </html>
    """)


def hi2_view(request):
    return render(request, 'hello.html')


def jurek_view(request):
    return HttpResponse("Witaj, Jurek!")


def jacek_view(request):
    return HttpResponse("Witaj, Jacek!")


def ksawier_view(request):
    return HttpResponse("Witaj, Ksawier!")


def name_view(request, name):
    return HttpResponse(name)
