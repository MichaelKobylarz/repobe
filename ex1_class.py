from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views import View
from .models import Contact
from .forms import ContactForm

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact_form.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    def put(self, request):
        contact = get_object_or_404(Contact, id=request.PUT.get('id'))
        form = ContactForm(request.PUT, instance=contact)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form updated successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    def delete(self, request):
        contact = get_object_or_404(Contact, id=request.DELETE.get('id'))
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully'})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])
