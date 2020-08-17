from django.db import models
from core import models as core_models


# Create your models here.
class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    review = models.TextField()  # Required
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # 모두 다 필수항목임
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # 메뉴 라인에 보이는 글자
    def __str__(self):
        return f"{self.review} - {self.room.name}"
        # return f"{self.review} - {self.room}"

        # return self.room.host.username
        # return self.review  # 객실의 리뷰

