from django.db import models
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """ Reservations Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CANCELED = "canceled"
    STATUS_CONFIRMED = "confirmed"

    STATUS = (
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
        (STATUS_PENDING, "Pending"),
    )
    status = models.CharField(choices=STATUS, max_length=80, default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE
    )  # User model을 가져올래
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

