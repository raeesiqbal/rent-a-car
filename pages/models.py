from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class City(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), null=True)
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Type(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    make = models.CharField(_("Make"), max_length=50)
    modal = models.CharField(_("Modal"), max_length=50)
    year = models.CharField(_("Year"), max_length=50)
    logo = models.ImageField(_("Logo"))
    content = models.TextField(_("Content"), null=True, blank=True)
    capacity = models.IntegerField(_("Capacity"))
    type = models.ForeignKey(Type, verbose_name=_("Type"), on_delete=models.CASCADE)
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.make}"


class PriceInterCity(models.Model):
    from_city = models.ForeignKey(
        City,
        verbose_name=_("From City"),
        on_delete=models.CASCADE,
        related_name="from_city",
    )
    to_city = models.ForeignKey(
        City,
        verbose_name=_("To City"),
        on_delete=models.CASCADE,
        related_name="to_city",
    )
    car = models.ForeignKey(Car, verbose_name=_("Car"), on_delete=models.CASCADE)
    price = models.CharField(_("Price"), max_length=100)
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.price}"


class PriceInCity(models.Model):
    city = models.ForeignKey(
        City,
        verbose_name=_("City"),
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(Car, verbose_name=_("Car"), on_delete=models.CASCADE)
    price = models.CharField(_("Price"), max_length=100)
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.price}"


Booking_Status = (
    ("Pending", "Pending"),
    ("In Progress", "In progress"),
    ("Completed", "Completed"),
    ("Cancelled", "Cancelled"),
)


class BookingInterCity(models.Model):
    name = models.CharField(_("Name"), max_length=999)
    address = models.CharField(_("Address"), max_length=999)
    pickup_date = models.CharField(_("Pickup Date"), max_length=999)
    pickup_time = models.CharField(_("Pickup Time"), max_length=999)
    phone = models.CharField(_("Phone"), max_length=50, null=True, blank=True)
    price = models.ForeignKey(
        PriceInterCity, verbose_name=_("Price"), on_delete=models.CASCADE
    )
    Status = models.CharField(
        _("Status"), max_length=99, choices=Booking_Status, default="Pending"
    )
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.name}"


class BookingInCity(models.Model):
    name = models.CharField(_("Name"), max_length=999)
    address = models.CharField(_("Address"), max_length=999)
    pickup_date = models.CharField(_("Pickup Date"), max_length=999)
    pickup_time = models.CharField(_("Pickup Time"), max_length=999)
    phone = models.CharField(_("Phone"), max_length=50, null=True, blank=True)
    price = models.ForeignKey(
        PriceInCity, verbose_name=_("Price"), on_delete=models.CASCADE
    )
    Status = models.CharField(
        _("Status"), max_length=99, choices=Booking_Status, default="Pending"
    )
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.name}"


class ContactUs(models.Model):
    name = models.CharField(_("Name"), max_length=999)
    email = models.CharField(_("Email"), max_length=999)
    phone = models.CharField(_("Phone"), max_length=999)
    subject = models.CharField(_("Subject"), max_length=999)
    message = models.TextField(_("Message"))
    date_posted = models.DateTimeField(_("Date Posted"), auto_now=True)

    def __str__(self):
        return f"{self.name}"
