from django.shortcuts import render, redirect

from form_app2.models import Message
from form_app2.forms import MessageForm


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


# django form
def contact_view_2(request):
    if request.method == "GET":
        form = MessageForm()  # unbound form

        return render(
            request,
            'form_app2/contact2.html',
            {'form': form}
        )

    elif request.method == "POST":
        data = request.POST

        # Walidacja danych
        form = MessageForm(data)  # bound form
        if form.is_valid():

            Message.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                category=form.cleaned_data.get('category'),
                subject=form.cleaned_data.get('subject'),
                body=form.cleaned_data.get('body'),
                date=form.cleaned_data.get('date'),
                time=form.cleaned_data.get('time')
            )

            return redirect('form_app2:contact_view_2')

        else:
            return render(
                request,
                'form_app2/contact2.html',
                {'form': form}
            )
