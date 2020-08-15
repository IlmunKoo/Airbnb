from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):  # User(models.Model)가 아님
    # docstring, 클래스 만들 때마다 이런 문구 넣어서 무슨 클래스인지 알려줌
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    bio = models.TextField(default="", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )  # max_length 필수, null이어도 괜찮다고 말해줌
    avatar = models.ImageField(null=True, blank=True)  # 사진

