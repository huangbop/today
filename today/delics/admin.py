from django.contrib import admin

from .models import Delic


class DelicAdmin(admin.ModelAdmin):
    model = Delic
    list_display = ('title', 'content', 'price', 'user', 'pub_date')


admin.site.register(Delic, DelicAdmin)
