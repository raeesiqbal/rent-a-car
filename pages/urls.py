from django.urls import path
from .views import *


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactView.as_view(), name="contact"),
    path("search", SearchView.as_view(), name="search"),
    path("city/<int:id>/<str:type>", CityRequest.as_view(), name="city"),
    path("booking", BookingRequest.as_view(), name="booking"),
]
