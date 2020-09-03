from django.db import models
from django.urls import reverse
from core import models as core_models  # model과 이름이 같으면 불편
from users import models as user_models
from django_countries.fields import CountryField

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:  # DB에는 등록x
        abstract = True

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class RoomType(AbstractItem):
    """ RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):  # 여러 번 사용되는 기능 상속해서 쓴다.
    """Room Model Definition"""

    name = models.CharField(max_length=140)  # 필수
    description = models.TextField()  # 필수()
    country = CountryField()
    city = models.CharField(max_length=80)  # 패키지 있지만 중요x, 그냥 max_length로 써줌
    price = models.IntegerField()  # DecimalField는 20.7같이 나오므로 그럴필요까진 없음
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 0시~24시, 날짜신경x DateTimeField와 다름
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)  # 즉시예약 가능한 경우
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))
        return 0

    # Foreign key: 일대다(many-to-one)관계
    # user는 1명, room은 여러 개 가질 수 있음
    # 인스타그램: 일대 다 관계,
    # user는 여러 post 가질 수 있지만, post는 오직 한 user만 가질 수 있음
    # 여러 비디오, 하나의 채널
    # host는 user여야 함, 어떤 모델과 다른 모델을 연결할 방법(foreign keys, 커넥션 필요, room과 user가 연결되어야 함)
    # 연결 완료
