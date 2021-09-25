from django.contrib import admin
from django.db import models
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation nAdmin Definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
