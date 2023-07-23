from django.urls import path, include

from .views import FlightView, ReservationView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('flight', FlightView)
router.register('reserviton', ReservationView)

urlpatterns = [
    path("", include(router.urls)),
]
