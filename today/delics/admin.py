from django.contrib import admin

from .models import Delic


class DelicAdmin(admin.ModelAdmin):
    model = Delic


admin.site.register(Delic, DelicAdmin)
