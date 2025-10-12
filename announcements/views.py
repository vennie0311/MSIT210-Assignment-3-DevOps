from django.shortcuts import render, get_object_or_404
from .models import Announcement

def home(request):
    return render(request, 'home.html')

def announcement_list(request):
    qs = Announcement.objects.order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': qs})

def announcement_detail(request, id):
    ann = get_object_or_404(Announcement, pk=id)
    return render(request, 'announcements/detail.html', {'announcement': ann})
