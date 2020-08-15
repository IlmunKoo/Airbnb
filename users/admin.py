from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)  # decorator
# admin패널에서 이 User를 보고 싶어! user를 컨트롤할 클래스가 바로 이게 될 거야 라는 의미
# decorator는 클래스 위에 있어야 작동
# CustomUserAdmin로 user를 컨트롤, 이 위에 오는 것으로 알 수 있음
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

