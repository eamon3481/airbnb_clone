from django.contrib import admin
from django.utils import timezone
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Def """

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
    )