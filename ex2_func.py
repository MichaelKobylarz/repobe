import logging
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notification
from .forms import NotificationForm

logger = logging.getLogger(__name__)

def notification_list(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    notifications = Notification.objects.all()
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def notification_detail(request, pk):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    notification = get_object_or_404(Notification, pk=pk)
    return render(request, 'notifications/notification_detail.html', {'notification': notification})

def notification_create(request):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm()
    return render(request, 'notifications/notification_form.html', {'form': form})

def notification_update(request, pk):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == "POST":
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'notifications/notification_form.html', {'form': form})

def notification_delete(request, pk):
    logger.info(f"Request method: {request.method}, Path: {request.path}")
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == "POST":
        notification.delete()
        return redirect('notification_list')
    return render(request, 'notifications/notification_confirm_delete.html', {'notification': notification})
