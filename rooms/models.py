from django.db import models
from core import models as core_models  # model과 이름이 같으면 불편
from users import models as user_models
from django_countries.fields import CountryField

# Create your models here.
class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)  # 필수
    description = models.TextField()  # 필수()
    country = CountryField()
    city = models.CharField(max_length=80)  # 패키지 있지만 중요x, 그냥 max_length로 써줌
    price = models.ImageField()  # DecimalField는 20.7같이 나오므로 그럴필요까진 없음
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 0시~24시, 날짜신경x DateTimeField와 다름
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)  # 즉시예약 가능한 경우
    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE
    )  # host는 user여야 함, 어떤 모델과 다른 모델을 연결할 방법(foreign keys, 커넥션 필요, room과 user가 연결되어야 함)
    # 연결 완료

