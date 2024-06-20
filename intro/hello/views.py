import datetime

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


# szablon
def hi2_view(request):
    return render(request, 'hello.html')


def jurek_view(request):
    return HttpResponse("Witaj, Jurek!")


def jacek_view(request):
    return HttpResponse("Witaj, Jacek!")


def ksawier_view(request):
    return HttpResponse("Witaj, Ksawier!")


# Podatność XSS - przykład
def name_view(request, name):
    # importy powinny być zawsze na samej górze
    from django.utils.html import escape

    # always remember to escape your output
    print(name)
    escaped_name = escape(name)
    print(escaped_name)

    return HttpResponse(f"Witaj, {name}!")


# kontekst szablonu
def name_view2(request, name):
    return render(
        request,
        'hello2.html',
        {"name": name}
    )


def is_it_new_year(request):

    today = datetime.date.today()
    if today.month == 1 and today.day == 1:
        msg = "TAK"
    else:
        msg = "NIE"

    return render(
        request,
        'isitnewyear.html',
        {'msg': msg}
    )