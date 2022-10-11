from django.contrib import admin
from .models import *

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_posted",
    )

    search_fields = [
        "name",
        "date_posted",
    ]


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_posted",
    )

    search_fields = [
        "name",
        "date_posted",
    ]


class CarAdmin(admin.ModelAdmin):
    list_display = (
        "make",
        "modal",
        "type",
        "year",
    )

    search_fields = [
        "make",
        "modal",
        "year",
        "type__name",
    ]
    raw_id_fields = ("type",)


class PriceInterCityAdmin(admin.ModelAdmin):
    list_display = (
        "from_city",
        "to_city",
        "car",
        "price",
    )
    search_fields = [
        "from_city",
        "to_city",
        "car__make",
        "car__modal",
        "car__year" "price",
    ]
    raw_id_fields = ("from_city", "to_city", "car")


class PriceInCityAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "car",
        "price",
    )
    search_fields = [
        "city",
        "car__make",
        "car__modal",
        "car__year",
        "price",
    ]
    raw_id_fields = ("city", "car")


class BookingInCityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "pickup_date",
        "pickup_time",
        "phone",
        "price",
    )
    search_fields = [
        "name",
        "address",
        "pickup_date",
        "pickup_time",
        "phone",
        "price__price",
    ]
    raw_id_fields = ("price",)


class BookingInterCityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "pickup_date",
        "pickup_time",
        "phone",
        "price",
    )
    search_fields = [
        "name",
        "address",
        "pickup_date",
        "pickup_time",
        "phone",
        "price__price",
    ]
    raw_id_fields = ("price",)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
        "subject",
    )
    search_fields = [
        "name",
        "phone",
        "email",
        "subject",
    ]


admin.site.register(City, CityAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(PriceInterCity, PriceInterCityAdmin)
admin.site.register(PriceInCity, PriceInCityAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(BookingInCity, BookingInCityAdmin)
admin.site.register(BookingInterCity, BookingInterCityAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
