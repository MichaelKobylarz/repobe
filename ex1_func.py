from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact_form.html', {'form': form})
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    elif request.method == 'PUT':
        contact = get_object_or_404(Contact, id=request.PUT.get('id'))
        form = ContactForm(request.PUT, instance=contact)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form updated successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    elif request.method == 'DELETE':
        contact = get_object_or_404(Contact, id=request.DELETE.get('id'))
        contact.delete()
        return JsonResponse({'message': 'Contact deleted successfully'})
    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])
