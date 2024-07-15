from django.shortcuts import render

from django import views
from django.views.generic import TemplateView


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
