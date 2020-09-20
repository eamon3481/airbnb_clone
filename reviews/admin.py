from django.contrib import admin
from . import models


@admin.register(models.Review)
class AdminReview(admin.ModelAdmin):

    """ AdminReview Def """

    list_display = ("__str__", "rating_average")