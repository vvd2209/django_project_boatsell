from django.contrib import admin

from boat.models import Owner, Boat, BoatHistory


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner',)
    list_filter = ('year', 'owner',)


@admin.register(BoatHistory)
class BoatHistoryAdmin(admin.ModelAdmin):
    list_display = ('boat', 'start_year', 'stop_year', 'owner',)
    list_filter = ('boat', 'owner',)


