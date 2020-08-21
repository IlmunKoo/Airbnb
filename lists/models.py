from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE
    )  # 유저 한명당 여러개 lsit 가능, list한명당 여러명의 유저? 가능하지않나?
    room = models.ManyToManyField(
        "rooms.Room", blank=""
    )  # 리스트는 여러개의 room 가질 수 있으므로, blank 허용

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.room.count()

    count_rooms.short_description = "Numbers of Rooms"

