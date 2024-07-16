from django.shortcuts import render, redirect

from django import views
from django.views.generic import TemplateView

from view_app import forms


# widok funkcyjny
def hello_view(request):
    if request.method == "GET":
        name = "Jan"
        return render(
            request,
            'view_app/hello.html',
            {
                "name": name
            }
        )


# widok klasowy
class HelloView(views.View):
    def get(self, request):
        name = "Jan"

        return render(
            request,
            'view_app/hello.html',
            {
                "name": name
            }
        )


# widok generyczny
class HelloTemplateView(TemplateView):
    template_name = 'view_app/hello.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Jan"

        return context


# C z CRUD (czyli Create)
# Widok funkcyjny
def person_create_view(request):
    if request.method == "GET":
        form = forms.PersonForm()

        return render(
            request,
            'view_app/create_person.html',
            {
                'form': form
            }
        )

    elif request.method == "POST":
        data = request.POST

        form = forms.PersonForm(data)

        if form.is_valid():
            form.save()

            return redirect('view_app:create_person_view')

        return render(
            request,
            'view_app/create_person.html',
            {
                'form': form
            }
        )


# Widok klasowy
class PersonCreateView(views.View):
    def get(self, request):
        form = forms.PersonForm()

        return render(
            request,
            'view_app/create_person.html',
            {
                'form': form
            }
        )

    def post(self, request):
        data = request.POST

        form = forms.PersonForm(data)

        if form.is_valid():
            form.save()

            return redirect('view_app:create_person_view2')

        return render(
            request,
            'view_app/create_person.html',
            {
                'form': form
            }
        )

