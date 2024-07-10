from django.shortcuts import render, redirect

from form_app2.models import Message


# 1. Formularz html
def contact_view_1(request):
    if request.method == "GET":
        return render(
            request,
            'form_app2/contact1.html',
        )
    elif request.method == "POST":
        data = request.POST

        # Walidacja danych
        ...

        Message.objects.create(
            name=data.get('name'),
            email= data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body'),
            date=data.get('date'),
            time=data.get('time')
        )

        return redirect('form_app2:contact_view_1')
