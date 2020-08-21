from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "count_rooms",
    )
    search_fields = ("name",)
    filter_horizontal = ("room",)

