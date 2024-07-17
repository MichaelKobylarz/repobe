from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


# Create your views here.
def index(request):

    # Lista użytkowników
    users = User.objects.all()
    print(users)

    # # Tworzenie użytkownika
    # User.objects.create_user(
    #     username='adam',
    #     password='tajne'
    # )

    # Uwierzytelnienie (zwraca obiekt użytkownika w przypadku powodzenia lub
    # None jeżeli uwierzytelnienie nie powiedzie się)
    user = authenticate(username='adam', password='tajne')
    print(user)

    # # logowanie = stworzenie uwierzytelnionej sesji
    # if user:
    #     login(request, user=user)

    # Jak wyciągnąc zalogowanego użytkownika?
    # request.user - obiekt zalogowanego użytkownika jeżeli
    # taki istnieje, w przeciwnym wypadku AnonymousUser
    print(request.user)

    # Jak wylogować aktualnie zalogowanego użytkownika
    logout(request)

    return render(
        request,
        'auth_app/index.html'
    )


def home(request):
    # gdybyśmy chcieli niedopuszczać niezalogowanych użytkowników
    # if not request.user.is_authenticated:
    #     return redirect('auth_app:login_view')

    return render(
        request,
        'auth_app/home.html'
    )


def login_view(request):
    if request.method == "GET":
        return render(
            request,
            'auth_app/login.html'
        )
    elif request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)

            return redirect('auth_app:home')

        return render(
            request,
            'auth_app/login.html'
        )


def logout_view(request):
    if request.method == "POST":
        logout(request)

    return redirect('auth_app:login_view')
