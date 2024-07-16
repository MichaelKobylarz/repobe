import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Notification
from .forms import NotificationForm

logger = logging.getLogger(__name__)

class LoggingView(View):
    def dispatch(self, request, *args, **kwargs):
        logger.info(f"Request method: {request.method}, Path: {request.path}")
        return super().dispatch(request, *args, **kwargs)

class NotificationListView(LoggingView):
    def get(self, request):
        notifications = Notification.objects.all()
        return render(request, 'notifications/notification_list.html', {'notifications': notifications})

class NotificationDetailView(LoggingView):
    def get(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk)
        return render(request, 'notifications/notification_detail.html', {'notification': notification})

class NotificationCreateView(LoggingView):
    def get(self, request):
        form = NotificationForm()
        return render(request, 'notifications/notification_form.html', {'form': form})

    def post(self, request):
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
        return render(request, 'notifications/notification_form.html', {'form': form})

class NotificationUpdateView(LoggingView):
    def get(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk)
        form = NotificationForm(instance=notification)
        return render(request, 'notifications/notification_form.html', {'form': form})

    def post(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk)
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
        return render(request, 'notifications/notification_form.html', {'form': form})

class NotificationDeleteView(LoggingView):
    def get(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk)
        return render(request, 'notifications/notification_confirm_delete.html', {'notification': notification})

    def post(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk)
        notification.delete()
        return redirect('notification_list')

# urls.py
from django.urls import path
from .views import (NotificationListView, NotificationDetailView, NotificationCreateView,
                    NotificationUpdateView, NotificationDeleteView)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('<int:pk>/', NotificationDetailView.as_view(), name='notification_detail'),
    path('new/', NotificationCreateView.as_view(), name='notification_create'),
    path('<int:pk>/edit/', NotificationUpdateView.as_view(), name='notification_update'),
    path('<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification_delete'),
]
