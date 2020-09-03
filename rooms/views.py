from django.views.generic import ListView
from django.http import Http404
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


# Create your views here.
class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "potato"
    context_object_name = "rooms"
    # 페이지 대신 원하는 글자를 넣을 수도 있음
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
