from django.shortcuts import render

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
