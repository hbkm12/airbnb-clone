from django.contrib import admin
from django.db import models
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation nAdmin Definition"""

    pass
