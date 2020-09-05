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
        country = request.GET.get("country", "KR")
        room_type = int(request.GET.get("room_type", 0))

        price = int(request.GET.get("price", 0))
        guests = int(request.GET.get("guests", 0))
        bedrooms = int(request.GET.get("bedrooms", 0))
        beds = int(request.GET.get("beds", 0))
        baths = int(request.GET.get("baths", 0))

        instant = request.GET.get("instant", False)
        super_host = request.GET.get("super_host", False)
        s_amenities = request.GET.getlist("amenities")
        s_facilities = request.GET.getlist("facilities")

        form = {  # request에서 받은 것들
            "city": city,
            "s_room_type": room_type,
            "s_country": country,
            "price": price,
            "guests": guests,
            "bedrooms": bedrooms,
            "beds": beds,
            "baths": baths,
            "s_amenities": s_amenities,
            "s_facilities": s_facilities,
            "instant": instant,
            "super_host": super_host,
            
        }

        room_types = models.RoomType.objects.all()
        amenities = models.Amenity.objects.all()
        facilities = models.Facility.objects.all()

        choices = {  # DB에서 받은 것들
            "countries": countries,
            "room_types": room_types,
            "amenities": amenities,
            "facilities": facilities,
        }
        return render(request, "rooms/search.html", {**form, **choices},)

