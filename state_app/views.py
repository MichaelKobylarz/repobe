from django.shortcuts import render, redirect


# Create your views here.
def cookies_view(request):

    # dostęp do ciasteczek
    cookies = request.COOKIES
    print(cookies)

    res = render(
        request,
        'state_app/cookies.html'
    )

    # żądanie ustawienia ciasteczka
    res.set_cookie("ciasteczko1", value=5)
    res.set_cookie("ciasteczko2", value=10, max_age=30)  # max_age - liczba sekund do wygaśniecia

    return res


def form_view(request):
    if request.method == "GET":
        return render(
            request,
            'state_app/form.html'
        )
    elif request.method == "POST":
        # 1. walidacja danych
        data = request.POST
        post = data.get('post')

        # jeżeli walidacja przeszła to zapisujemy.
        # 2. Zapis
        ...

        # 3. Przekierowanie
        res = redirect('state_app:home_view')
        res.set_cookie('msg', "Pomyslnie zapisano post.")

        return res


def home_view(request):
    cookies = request.COOKIES
    msg = cookies.get('msg')

    res = render(
        request,
        'state_app/home.html',
        {
            'msg': msg
        }
    )

    res.delete_cookie('msg')

    return res


# Framework messages
# https://docs.djangoproject.com/en/5.0/ref/contrib/messages/


def session_view(request):
    # odczyt z sesji
    print(dict(request.session))

    # zapis do sesji (automatycznie powoduje powstanie sesji, jeżeli taka nie istnieje)
    request.session['klucz'] = 'wartosc'

    counter = request.session.get('num_visit', 0)
    request.session['num_visit'] = counter + 1

    return render(
        request,
        'state_app/session.html',
        {
            'counter': counter + 1
        }
    )
