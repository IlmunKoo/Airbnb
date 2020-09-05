from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.urls import reverse
from django_countries import countries
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


class RoomDetail(DetailView):
    """ RoomDetail Definition """

    model = models.Room

    def search(request):
        city = request.GET.get("city", "Anywhere")
        city = str.capitalize(city)
        room_types = models.RoomType.objects.all()

        return render(
            request,
            "rooms/search.html",
            {"city": city, "countries": countries, "room_types": room_types},
        )

