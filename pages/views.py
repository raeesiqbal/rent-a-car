from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import *
from django.contrib import messages


class HomeView(View):
    def get(self, request, *args, **kwargs):
        from_city = City.objects.get(name="Lahore")
        to_city = City.objects.get(name="Islamabad")
        get_cars = PriceInterCity.objects.filter(from_city=from_city, to_city=to_city)
        li_list = []
        for car in get_cars:
            if car.car.type.name == "sedan":
                if "sedan" not in li_list:
                    li_list.append("sedan")
            if car.car.type.name == "suv":
                print("ok")
                if "suv" not in li_list:
                    li_list.append("suv")
            if car.car.type.name == "hatchback":
                if "hatchback" not in li_list:
                    li_list.append("hatchback")
        context = {
            "cars": get_cars,
            "li_list": li_list,
        }
        return render(request, "index.html", context=context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/contact.html")

    def post(self, request, *args, **kwargs):
        contact = ContactUs.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            email=request.POST["email"],
            message=request.POST["message"],
            subject=request.POST["subject"],
        )
        messages.success(
            request, f"Your request has been received. Your request id is:{contact.id}"
        )
        return redirect("pages:home")


class SearchView(View):
    def get(self, request, *args, **kwargs):
        return redirect("pages:home")

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if request.POST["type"] == "Yes":
            from_city = City.objects.get(name=request.POST["from"])
            to_city = City.objects.get(name=request.POST["to"])
            get_cars = PriceInterCity.objects.filter(
                from_city=from_city, to_city=to_city
            )
            context = {
                "cars": get_cars,
                "li_list": None,
                "href": True,
                "city": "Lahore",
                "from": request.POST["from"],
                "to": request.POST["to"],
                "intercity": "on",
            }
        else:
            city = City.objects.get(name=request.POST["city"])
            get_cars = PriceInCity.objects.filter(city=city)
            context = {
                "cars": get_cars,
                "li_list": None,
                "href": True,
                "city": request.POST["city"],
                "from": "Lahore",
                "to": "Islamabad",
                "intercity": "off",
            }
        li_list = []
        for car in get_cars:
            if car.car.type.name == "sedan":
                if "sedan" not in li_list:
                    li_list.append("sedan")
            if car.car.type.name == "suv":
                if "suv" not in li_list:
                    li_list.append("suv")
            if car.car.type.name == "hatchback":
                if "hatchback" not in li_list:
                    li_list.append("hatchback")
        context.update({"li_list": li_list})
        return render(request, "index.html", context=context)


class CityRequest(APIView):
    def get(self, request, id, type):
        if type == "Yes":
            intercity_price = PriceInterCity.objects.get(id=id)
            city = intercity_price.to_city
        if type == "No":
            in_city_price = PriceInCity.objects.get(id=id)
            city = in_city_price.city
        serializer = CitySerializer(city)
        return JsonResponse(
            {"data": serializer.data},
            status=status.HTTP_200_OK,
        )


class BookingRequest(APIView):
    def post(self, request):
        name = request.POST["name"]
        address = request.POST["address"]
        date = request.POST["date"]
        time = request.POST["time"]
        booking_id = request.POST["booking_price_id"]
        booking_type = request.POST["booking_type"]
        phone = request.POST["phone"]
        if booking_type == "Yes":
            price = PriceInterCity.objects.get(id=booking_id)
            booking = BookingInterCity.objects.create(
                name=name,
                address=address,
                pickup_date=date,
                pickup_time=time,
                price=price,
                phone=phone,
            )
            serializer = BookingInterCitySerializer(booking)
        elif booking_type == "No":
            price = PriceInCity.objects.get(id=booking_id)
            booking = BookingInCity.objects.create(
                name=name,
                address=address,
                pickup_date=date,
                pickup_time=time,
                price=price,
            )
            serializer = BookingInCitySerializer(booking)

        if booking:
            return JsonResponse(
                {"data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"data": None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
